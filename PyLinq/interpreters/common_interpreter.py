from PyLinq.proxy import FuncProxy
from PyLinq.parser.nodes import *


# 聚合函数字典
agg_funcs = dict()
# 聚合函数在 select 语句的哪个位置
agg_position = set()


def visit_index(expr, data_sources):
    index_dict = {}
    make_index_dict(expr, data_sources, index_dict)
    name, index_looped = index_dict.popitem()
    index_len = len(index_dict)
    for index_key, instances in index_looped.items():
        for instance in get_index_instance(index_key, set(), index_dict, {}, 0, index_len):
            for front_instance in instances:
                instance[name] = front_instance
                yield instance


def get_index_instance(index_key, used_keys, index_dict, instance_dict, num, index_num):
    if num == index_num:
        yield instance_dict.copy()
    else:
        # 只取一个
        table_name, index = next(filter(lambda x: x[0] not in used_keys, index_dict.items()))
        used_keys.add(table_name)
        for instance in index.get(index_key, []):
            instance_dict[table_name] = instance
            for new_instance_dict in get_index_instance(index_key, used_keys, index_dict, instance_dict, num + 1, index_num):
                yield new_instance_dict
            del instance_dict[table_name]
        used_keys.remove(table_name)


def make_index_dict(index_expr, data_sources, index_dict):
    """
    :param index_expr: 索引表达式
    :param data_sources: {
        'student': [
                     {'name': 'jay_chou', 'age': 40},
                     {'name': 'zhang_xx', 'age': 30}
                   ],
        'teacher': [
                     {'name': 'xxx', 'year': 4},
                     {'name': 'yyy', 'year': 5}
                   ]
    }
    :param index_dict: 索引字典
    :return:
    """
    if isinstance(index_expr, SQLToken):
        if index_expr.tag == FUNC and index_expr.args[0] == '=':
            make_index_dict(index_expr.args[1], data_sources, index_dict)
            make_index_dict(index_expr.args[2], data_sources, index_dict)
        else:
            raise SyntaxError('不支持该索引语法')
    elif isinstance(index_expr, VAR):
        name = visit(index_expr.name, data_sources, None, None)
        if name in data_sources:
            instances = data_sources.pop(name)
            attr = visit(index_expr.attr, data_sources, None, None)
            temp_dict = {}
            for instance in instances:
                temp_dict.setdefault(instance[attr], []).append(instance)
            index_dict[name] = temp_dict
    elif isinstance(index_expr, list):
        for sub_expr in index_expr:
            make_index_dict(sub_expr, data_sources, index_dict)


def visit_select(select_expr: tuple, instance_dict, env):
    """
    :param instance_dict:
    :param env:
    :param select_expr: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    res = {}
    # * 表达式
    if select_expr[1]:
        for table_name, values in instance_dict.items():
            for key, value in values.items():
                res[key] = value
        return res

    for i, expr in enumerate(select_expr[2:]):
        # 不存在聚合函数
        if not agg_position:
            key, value = make_name(expr, visit(expr, instance_dict, env))
            res[key] = value
        elif expr.tag == FUNC:
            res = make_name(expr, visit(expr, instance_dict, env, i))
        else:
            key, value = make_name(expr, visit(expr, instance_dict, env, i))
            res[key] = value
    return res


def make_name(expr, value):
    if isinstance(expr, VAR):
        if expr.attr:
            return expr.attr.value, value
        return expr.name.value, value
    if isinstance(expr, SQLToken):
        if expr.tag == FUNC and expr.args[0] not in FuncProxy.aggr:
            return expr.args[0], value
    return value


def init_aggfuncs(expr, i=None):
    if i is None:
        for i, expr in enumerate(expr[2:]):
            init_aggfuncs(expr, i)
    elif isinstance(expr, SQLToken):
        if expr.tag == FUNC and expr.args[0] in FuncProxy.aggr:
            func_name = expr.args[0] + str(i)
            agg_funcs[func_name] = FuncProxy.get(expr.args[0])
            agg_position.add(i)
        else:
            for sub_expr in expr.args:
                init_aggfuncs(sub_expr, i)


def visit_limit(limit_expr: SQLToken, res: list, env) -> list:
    offset, limit = visit(limit_expr.args[0], res, env), visit(limit_expr.args[1], res, env)
    return res[offset:offset+limit]


def visit_tables(tables_expr: SQLToken, data_sources: dict, env: dict, index) -> dict:
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
    return dict(make_name(table_expr, visit(table_expr, data_sources, env, index)) for table_expr in tables_expr.args)


def visit_inner(inner_expr: SQLToken, data_sources: dict, env: dict, index) -> tuple:
    """
    inner_expr: Token(
        tag='inner',
        args=(
            var(name=const(value='mobile'), attr=None, func=None),
            Token(
                tag='func',
                args=(
                    '=',
                    var(name=const(value='company'), attr=const(value='id'), func=None),
                    var(name=const(value='mobile'), attr=const(value='company_id'), func=None)
                )
            )
        )
    )
    """
    args = inner_expr.args
    if isinstance(args, VAR):
        return args.name.value, visit(args, data_sources, env, index)
    env.setdefault('index', []).append(args[1])
    return args[0].name.value, visit(args[0], data_sources, env, index)


def visit_as(as_expr: SQLToken, data_sources, env, index) -> tuple:
    """
    :param index:
    :param env:
    :param as_expr:
    :param data_sources: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    new_name = visit(as_expr.args[1], data_sources, env, index)
    return new_name, visit(as_expr.args[0], data_sources, env, index)


def visit_var(var_expr: VAR, data_sources: dict, env: dict, index):
    name = visit(var_expr.name, data_sources, env, index)
    table = data_sources[name]
    attr = visit(var_expr.attr, data_sources, env, index)
    if not attr:
        return table
    func = visit(var_expr.func, data_sources, env, index)
    value = table[attr]
    return FuncProxy.get(func)(value) if func else value


def func_star(data_sources):
    return (v for table_name, column in data_sources.items() for attr, v in column.items())


def visit_func(func_expr: SQLToken, data_sources, env, index):
    name = func_expr.args[0]

    if index is not None and index in agg_position:
        func = agg_funcs.get(name + str(index))
        if func is None:
            func = FuncProxy.get(name)
    else:
        func = FuncProxy.get(name)

    args = []
    for arg in func_expr.args[1:]:
        arg = visit(arg, data_sources, env, index)
        if arg == '*':
            for v in func_star(data_sources):
                args.append(v)
        else:
            args.append(arg)
    return func(*args)


def visit_const(const_expr: CONST, data_sources, env, index):
    """
    返回常量
    """
    return const_expr.value


def visit_link(link_expr: SQLToken, data_sources, env, index) -> list:
    """
    链接接子 SELECT 语句
    """
    res = []
    for instance in env[link_expr.args]:
        line = tuple(v for k, v in instance.items())
        res.append(line[0] if len(line) == 1 else line)
    return res


def visit_case(case_expr: SQLToken, data_sources: dict, env, index):
    """
    :param index:
    :param env:
    :param case_expr:
    :param data_sources: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    for condition, value in case_expr.args:
        if condition is None or visit(condition, data_sources, env, index):
            return visit(value, data_sources, env, index)


def visit(sql_expr, data_sources, env, index=None):
    if sql_expr is None:
        return None
    if isinstance(sql_expr, STATES):
        return visit_dict[sql_expr.__class__](sql_expr, data_sources, env, index)
    if isinstance(sql_expr, SQLToken):
        return visit_dict[sql_expr.tag](sql_expr, data_sources, env, index)
    if isinstance(sql_expr, (list, tuple, set)):
        if len(sql_expr) == 1:
            return visit(sql_expr[0], data_sources, env, index)
        return (visit(sub_expr, data_sources, env, index) for sub_expr in sql_expr)


visit_dict = {
    TABLES: visit_tables,
    VAR: visit_var,
    INNER: visit_inner,
    CONST: visit_const,
    AS: visit_as,
    FUNC: visit_func,
    LINK: visit_link,
    CASE: visit_case,
}
