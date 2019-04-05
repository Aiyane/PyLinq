from antlr4 import CommonTokenStream, InputStream

from gen.MySqlLexer import MySqlLexer
from gen.MySqlParser import MySqlParser

from PyLinq.visitor import MySqlVisitor
from PyLinq.proxy import FuncProxy
from PyLinq.nodes import *

agg_funcs = dict()


def get_expr(expr):
    """
    只用来获取语句的参数
    """
    if expr is None:
        return None
    if isinstance(expr, SQLToken):
        return get_expr_dict[expr.tag](expr)
    return get_expr_dict[expr.__class__](expr)


def get_var(var_expr: VAR) -> list:
    name, attr = get_expr(var_expr.name), get_expr(var_expr.attr)
    if attr:
        return [0, name, attr]
    return [0, name, None]


def get_desc(desc_expr: SQLToken) -> list:
    val: list = get_expr(desc_expr.args)
    val[0] = 1
    return val


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
    table = data_sources[name]
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
        if has_aggfunc(expr):
            if expr.tag == AS:
                key, value = visit_as(expr, data_sources, str(i))
            else:
                key, value = expr.args[0], visit_aggfunc(expr, data_sources, str(i))
            res[key] = value
        elif isinstance(expr, SQLToken) and expr.tag == FUNC:
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


def visit_func(func_expr: SQLToken, data_sources):
    func = FuncProxy.get(func_expr.args[0])
    if func is None:
        raise TypeError(f"没有内置函数 `{func_expr.args[0]}`")
    args = []
    for arg in func_expr.args[1:]:
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
}

get_expr_dict = {
    VAR: get_var,
    CONST: visit_const,
    DESC: get_desc,
}


def main_loop(res_list: ResList, data_sources: dict, instance_dict, res: list) -> list:
    """
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
    if res_list.condition:
        if res_list.having_expr:
            if visit(res_list.condition, instance_dict) and visit(res_list.having_expr, instance_dict):
                res.append(visit_select(res_list.select_expr, instance_dict))
        else:
            if visit(res_list.condition, instance_dict):
                res.append(visit_select(res_list.select_expr, instance_dict))
    else:
        res.append(visit_select(res_list.select_expr, instance_dict))
    return res


def has_aggfunc(expr) -> bool:
    if isinstance(expr, SQLToken):
        if expr.tag == FUNC and expr[0] in FuncProxy.aggr:
            return True
        if expr.tag == AGGFUNC:
            return True
        if expr.tag == AS:
            return has_aggfunc(expr.args[0])
    return False


def init_aggfuncs(expr, i=None):
    if isinstance(expr, SQLToken) and i is not None:
        if expr.tag == AGGFUNC:
            agg_funcs[expr.args[0] + str(i)] = FuncProxy.get(expr.args[0])
        elif expr.tag == FUNC and expr.args[0] in FuncProxy.aggr:
            agg_funcs[expr.args[0] + str(i)] = FuncProxy.get(expr.args[0])
        elif expr.tag == AS:
            sub_expr = expr.args[0]
            init_aggfuncs(sub_expr, i)
    elif isinstance(expr, tuple):
        for i, expr in enumerate(expr[2:]):
            init_aggfuncs(expr, i)


def sql_interpreter(sql_expr: SELECT, data_sources: dict) -> list:
    """
    :param sql_expr:
    :param data_sources:
    :return:
    """
    data_sources = visit(sql_expr.from_expr.tables, data_sources)
    from_expr = sql_expr.from_expr
    res_list = ResList([], from_expr.condition, from_expr.having, sql_expr.select)
    limit = sql_expr.limit

    # 构造聚合函数
    init_aggfuncs(sql_expr.select)

    res = main_loop(res_list, data_sources, {}, [])
    # 如果有聚合函数
    if agg_funcs:
        agg_funcs.clear()
        return [res[-1]]
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
