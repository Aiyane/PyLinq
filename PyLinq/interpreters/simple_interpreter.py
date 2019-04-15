from .common_interpreter import *


def run(expr: EXPR, data_sources: dict, env: dict) -> list:
    """
    无 group 与 order 语句
    """
    # 执行 from 筛选
    data_sources = visit(expr.from_expr, data_sources, env)
    # 通过 select 语句先确定有哪些聚合函数，每一列的都需要新生成一个函数
    init_aggfuncs(expr.select_expr)
    res = index_loop(expr, data_sources, env, []) if expr.index_expr else main_loop(expr, data_sources, {}, [], env)

    # 如果有聚合函数
    if agg_position:
        agg_funcs.clear()
        agg_position.clear()
        try:
            return res[-1] if isinstance(res[-1], list) else [res[-1]]
        except IndexError:
            return []

    # limit 语句
    if expr.limit_expr:
        return visit_limit(expr.limit_expr, res, env)

    return res


def index_loop(expr, data_sources, env, res):
    for instance_dict in visit_index(expr, data_sources):
        if data_sources:
            main_loop(expr, data_sources.copy(), instance_dict, res, env)
        else:
            condition_filter(expr, instance_dict, res, env)
    return res


def condition_filter(expr: EXPR, instance_dict, res: list, env):
    """
    :param env:
    :param expr:
    :param instance_dict: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :param res: 结果列表
    :return: 结果列表
    """
    if (not expr.where_expr) or visit(expr.where_expr, instance_dict, env):
        res.append(visit_select(expr.select_expr, instance_dict, env))


def main_loop(expr: EXPR, data_sources: dict, instance_dict, res: list, env) -> list:
    """
    :param env:
    :param expr:
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
            condition_filter(expr, instance_dict, res, env)
        else:
            main_loop(expr, data_sources.copy(), instance_dict, res, env)
        # 处理完将本条记录删除
        del instance_dict[name]
    return res
