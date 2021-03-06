from .group_base_interpreter import *


def run(expr: EXPR, data_sources: dict, env: dict) -> list:
    """
    无 order 语句
    """
    # 执行 from 筛选
    data_sources = visit(expr.from_expr, data_sources, env)
    # 通过 select 语句先确定有哪些聚合函数，每一列的都需要新生成一个函数
    init_aggfuncs(expr.select_expr)

    data_sources, res = visit_group(expr, data_sources, env), []
    for pk, data_source in data_sources.items():
        condition_filter(expr, {pk: data_source}, res, env)

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


def condition_filter(expr: EXPR, instance_dict, res: list, env):
    if (not expr.having_expr) or expr.having_expr and group_visit(expr.having_expr, instance_dict, env):
        res.append(group_visit_select(expr.select_expr, instance_dict, env))
