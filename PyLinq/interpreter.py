from antlr4 import CommonTokenStream, InputStream
from copy import deepcopy

from gen.MySqlLexer import MySqlLexer
from gen.MySqlParser import MySqlParser

from PyLinq.visitor import MySqlVisitor
from PyLinq.proxy import FuncProxy
from PyLinq.nodes import *


# 聚合函数字典
agg_funcs = dict()
# 聚合函数在 select 语句的哪个位置
agg_position = set()
# group 语句
pks = set()


def visit_tables(tables_expr: SQLToken, data_sources: dict) -> dict:
    """
    data_sources 是
    {
        'student': [
                     {'name': 'jay_chou', 'age': 40},
                     {'name': 'zhang_xx', 'age': 30}
                   ],
        'teacher': [
                     {'name': 'xxx', 'year': 4},
                     {'name': 'yyy', 'year': 5}
                   ]
    } 这样的表数据, 返回
    {
        'student': [
                     {'name': 'jay_chou', 'age': 40},
                     {'name': 'zhang_xx', 'age': 30}
                   ]
    } 某些表数据结果
    """
    return dict(visit(table_expr, data_sources) for table_expr in tables_expr.args)


def visit_var(var_expr: VAR, data_sources: dict) -> tuple:
    """ 三种情况
    1.
    var 如果是 'student', 那么 data_sources 是
    {
        'student': [
                     {'name': 'jay_chou', 'age': 40},
                     {'name': 'zhang_xx', 'age': 30}
                   ],
        'teacher': [
                     {'name': 'xxx', 'year': 4},
                     {'name': 'yyy', 'year': 5}
                   ]
    } 这样的表数据, 返回
        ('student', [
                      {'name': 'jay_chou', 'age': 40},
                      {'name': 'zhang_xx', 'age': 30}
                    ]
        )

    2.
    var 如果是 'student.name', 那么 data_sources 只会是
    {
        'student': {'name': 'jay_chou', 'age': 40}
    } 这样一行数据. 返回
        ('name': 'jay_chou')

    3.
    var 如果是 'student.name.first', 那么 data_sources 只会是
    {
        'student': {'name': 'jay_chou', 'age': 40}
    } 这样一行数据. 返回
        ('name': 'j')
    其中 first 被认为是一个函数
    """
    name = visit(var_expr.name, data_sources)
    try:
        table = data_sources[name]
    except KeyError:
        return name, ''
    attr, func = visit(var_expr.attr, data_sources), visit(var_expr.func, data_sources)
    if attr:
        value = table[attr]
        return attr, FuncProxy.get(func)(value) if func else value
    return name, table


def visit_const(const_expr: CONST, data_sources=None):
    """返回常量"""
    return const_expr.value


def visit_inner(inner_expr: SQLToken, data_surces: dict):
    """
    inner 语句被视为默认的, 直接返回子语句结果
    """
    return visit(inner_expr.args, data_surces)


def visit_select(select_expr: tuple, data_sources) -> dict:
    """
    :param select_expr:
    :param data_sources: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    distinct, star = select_expr[0], select_expr[1]
    res = {}
    if star:
        for table_name, values in data_sources.items():
            for key, value in values.items():
                res[key] = value
        return res

    for i, expr in enumerate(select_expr[2:]):
        if i in agg_position:
            if expr.tag == AS:
                key, value = visit_as(expr, data_sources, str(i))
                res[key] = value
            else:
                key, value = expr.args[0], visit_aggfunc(expr, data_sources, str(i))
                res = value
        elif isinstance(expr, SQLToken) and (expr.tag == FUNC or expr.tag == AGGFUNC):
            res[expr.args[0]] = visit(expr, data_sources)
        else:
            key, value = visit(expr, data_sources)
            res[key] = value
    return res


def visit_as(as_expr: SQLToken, data_sources, str_i=None) -> tuple:
    """
    :param str_i: 给聚合函数使用
    :param as_expr:
    :param data_sources: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    if str_i is None:
        res = visit(as_expr.args[0], data_sources)
    else:
        if as_expr.args[0].tag == AGGFUNC:
            res = visit_aggfunc(as_expr.args[0], data_sources, str_i)
        elif as_expr.args[0].tag == AS:
            _, res = visit_as(as_expr.args[0], data_sources, str_i)
        else:
            raise ValueError("语法错误！")
    rename = visit(as_expr.args[1], data_sources)
    return rename, res[1] if isinstance(as_expr.args[0], VAR) else res


def func_star(data_sources):
    for table_name, column in data_sources.items():
        for attr, v in column.items():
            if (table_name, attr) not in pks:
                return v


def visit_func(func_expr: SQLToken, data_sources):
    func = FuncProxy.get(func_expr.args[0])
    if func is None:
        raise TypeError(f"没有内置函数 `{func_expr.args[0]}`")
    args = []
    for arg in func_expr.args[1:]:
        if arg == '*':
            args.append(func_star(data_sources))
        else:
            _arg = visit(arg, data_sources)
            args.append(_arg[1] if isinstance(arg, VAR) else _arg)
    return func(*args)


def visit_aggfunc(aggfunc_expr: SQLToken, data_sources, str_i):
    func = agg_funcs.get(aggfunc_expr.args[0] + str_i)
    if func is None:
        raise TypeError(f"没有内置函数 `{aggfunc_expr.args[0]}`")
    args = []
    for arg in aggfunc_expr.args[1:]:
        _arg = visit(arg, data_sources)
        if _arg == '*':
            args.append(data_sources)
        else:
            args.append(_arg[1] if isinstance(arg, VAR) else _arg)
    return func(*args)


def visit_limit(limit_expr: SQLToken, res: list) -> list:
    offset, limit = visit(limit_expr.args[0], res), visit(limit_expr.args[1], res)
    return res[offset:offset+limit]


def visit_link(link_expr: SQLToken, data_sources) -> list:
    res = []
    for instance in __SQL_RESULT__[link_expr.args]:
        line = tuple(v for k, v in instance.items())
        if len(line) == 1:
            res.append(line[0])
        else:
            res.append(line)
    return res


def visit_case(case_expr: SQLToken, data_sources: dict):
    """
    :param case_expr:
    :param data_sources: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    for condition, value in case_expr.args:
        if condition is None or visit(condition, data_sources):
            return visit(value, data_sources)


def visit(sql_expr, data_sources):
    if sql_expr is None:
        return None
    if isinstance(sql_expr, STATES):
        return tag_visit_dict[sql_expr.__class__](sql_expr, data_sources)
    if isinstance(sql_expr, SQLToken):
        return tag_visit_dict[sql_expr.tag](sql_expr, data_sources)
    if isinstance(sql_expr, (list, tuple, set)):
        return (visit(sub_expr, data_sources) for sub_expr in sql_expr)


tag_visit_dict = {
    TABLES: visit_tables,
    VAR: visit_var,
    INNER: visit_inner,
    CONST: visit_const,
    AS: visit_as,
    FUNC: visit_func,
    LIMIT: visit_limit,
    LINK: visit_link,
    AGGFUNC: visit_func,
    CASE: visit_case,
}


def main_loop(res_list: ResList, data_sources: dict, instance_dict, res: list) -> list:
    """
    :param has_group:
    :param res_list:
    :param data_sources: {
        'student': [
                     {'name': 'jay_chou', 'age': 40},
                     {'name': 'zhang_xx', 'age': 30}
                   ],
        'teacher': [
                     {'name': 'xxx', 'year': 4},
                     {'name': 'yyy', 'year': 5}
                   ]
    } 这样的表数据
    :param instance_dict: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :param res:
    :return:
    """
    # 取出一张表
    name, instances = data_sources.popitem()
    for instance in instances:
        instance_dict[name] = instance
        # 如果是最后一张表,处理一行,否则取出下一张表
        if not data_sources:
            condition_filter(res_list, instance_dict, res)
        else:
            main_loop(res_list, data_sources.copy(), instance_dict, res)
        # 处理完将本条记录删除
        del instance_dict[name]
    return res


def condition_filter(res_list: ResList, instance_dict, res: list) -> list:
    """
    :param res_list:
    :param instance_dict: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :param res: 结果列表
    :return: 结果列表
    """
    order = res_list.order_expr
    if res_list.condition:
        if res_list.having_expr:
            if visit(res_list.condition, instance_dict) and visit(res_list.having_expr, instance_dict):
                # item = visit_select(res_list.select_expr, instance_dict)
                if order:
                    index = bisect_left(res, instance_dict, order)
                    res.insert(index, instance_dict.copy())
                else:
                    res.append(visit_select(res_list.select_expr, instance_dict))
        else:
            if visit(res_list.condition, instance_dict):
                # item = visit_select(res_list.select_expr, instance_dict)
                if order:
                    index = bisect_left(res, instance_dict, order)
                    res.insert(index, instance_dict.copy())
                else:
                    res.append(visit_select(res_list.select_expr, instance_dict))
    else:
        if res_list.having_expr:
            if visit(res_list.having_expr, instance_dict):
                # item = visit_select(res_list.select_expr, instance_dict)
                if order:
                    index = bisect_left(res, instance_dict, order)
                    res.insert(index, instance_dict.copy())
                else:
                    res.append(visit_select(res_list.select_expr, instance_dict))
        else:
            # item = visit_select(res_list.select_expr, instance_dict)
            if order:
                index = bisect_left(res, instance_dict, order)
                res.insert(index, instance_dict.copy())
            else:
                res.append(visit_select(res_list.select_expr, instance_dict))
    return res


def init_aggfuncs(expr, i=None):
    if isinstance(expr, SQLToken) and i is not None:
        if expr.tag == AGGFUNC or (expr.tag == FUNC and expr.args[0] in FuncProxy.aggr):
            agg_funcs[expr.args[0] + str(i)] = FuncProxy.get(expr.args[0])
            agg_position.add(i)
        elif expr.tag == AS:
            sub_expr = expr.args[0]
            init_aggfuncs(sub_expr, i)
    elif isinstance(expr, tuple):
        for i, expr in enumerate(expr[2:]):
            init_aggfuncs(expr, i)


def bisect_left(a, x, orders, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.

    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if _compare(a[mid], x, orders): lo = mid+1
        else: hi = mid
    return lo


def _compare(item1, item2, orders):
    """比较函数"""
    for order, table_name, attr in orders:
        v1 = item1[table_name][attr]
        v2 = item2[table_name][attr]
        if v1 < v2:
            return True if order == 0 else False
        if v1 > v2:
            return False if order == 0 else True
    return True


def get_var(var_expr: VAR):
    """
    :param var_expr:
    :param instance_dict: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    }
    :return:
    """
    return visit(var_expr.name, None), visit(var_expr.attr, None)


def get_groups(expr):
    return set(get_var(sub_expr) for sub_expr in expr)


def get_desc_or_var(expr):
    if isinstance(expr, VAR):
        return (0, *get_var(expr))
    return (1, *get_var(expr.args))


def get_order(expr):
    if expr is None:
        return None
    return tuple(get_desc_or_var(sub_expr) for sub_expr in expr)


def visit_group(group_expr, data_sources):
    groups = get_groups(group_expr)
    res_dict = {}
    res = []
    i = 0
    for instance_dict in group_loop(data_sources, {}):
        _pk = []
        for table_name, attr in groups:
            try:
                _pk.append(instance_dict[table_name][attr])
            except KeyError:
                _pk.append(None)
        pk = tuple(_pk)
        if pk not in pks:
            pks.add(pk)
            res_dict[pk] = i
            for table_name, pure_instance_dict in instance_dict.items():
                for attr in pure_instance_dict.keys():
                    if (table_name, attr) not in groups:
                        instance_dict[table_name][attr] = [pure_instance_dict[attr]]
            res.append(instance_dict)
            i += 1
        else:
            for table_name, pure_instance in res[res_dict[pk]].items():
                for attr in pure_instance.keys():
                    if (table_name, attr) not in groups:
                        # print(instance_dict)
                        try:
                            pure_instance[attr].append(instance_dict[table_name][attr])
                        except KeyError:
                            pass
    return res


def group_loop(data_sources: dict, instance_dict) -> list:
    """
    :param has_group:
    :param res_list:
    :param data_sources: {
        'student': [
                     {'name': 'jay_chou', 'age': 40},
                     {'name': 'zhang_xx', 'age': 30}
                   ],
        'teacher': [
                     {'name': 'xxx', 'year': 4},
                     {'name': 'yyy', 'year': 5}
                   ]
    } 这样的表数据
    :param instance_dict: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :param res:
    :return:
    """
    # 取出一张表
    name, instances = data_sources.popitem()
    for instance in instances:
        instance_dict[name] = instance
        # 如果是最后一张表,处理一行,否则取出下一张表
        if not data_sources:
            yield deepcopy(instance_dict)
        else:
            for res in group_loop(data_sources, instance_dict):
                yield res
        # 处理完将本条记录删除
        del instance_dict[name]


def sql_interpreter(sql_expr: SELECT, data_sources: dict) -> list:
    """
    :param sql_expr:
    :param data_sources:
    :return:
    """
    data_sources = visit(sql_expr.from_expr.tables, data_sources)
    from_expr = sql_expr.from_expr
    res_list = ResList([], from_expr.condition, from_expr.having, sql_expr.select, get_order(sql_expr.order))
    limit = sql_expr.limit

    group_expr = from_expr.group
    if group_expr:
        data_sources, res = visit_group(group_expr, data_sources), []
        for data_source in data_sources:
            condition_filter(res_list, data_source, res)
        pks.clear()
    else:
        # 构造聚合函数
        init_aggfuncs(sql_expr.select)
        res = main_loop(res_list, data_sources, {}, [])
        # 如果有聚合函数
        if agg_funcs:
            agg_funcs.clear()
            agg_position.clear()
            return res[-1] if isinstance(res[-1], list) else [res[-1]]
    # 如果有排序
    if res_list.order_expr:
        res = [visit_select(res_list.select_expr, instance_dict) for instance_dict in res]
    return visit(limit, res) if limit else res


__SQL_RESULT__ = dict()


def run(sql_expr: str, data_sources: dict):
    """接口"""
    input_stream = InputStream(sql_expr)
    lexer = MySqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    visitor = MySqlVisitor()
    tree = parser.queryExpression()
    visitor.visit(tree)
    queue = visitor.select_statements_queue
    result = []
    # =================打印时间===================
    import time
    now = time.time()
    while not queue.empty():
        sql_expr: SelectStatement = queue.get()
        result = sql_interpreter(sql_expr.tree, data_sources)
        __SQL_RESULT__[sql_expr.id] = result
    print('运行时间:', time.time() - now)
    # ===========================================
    return result
