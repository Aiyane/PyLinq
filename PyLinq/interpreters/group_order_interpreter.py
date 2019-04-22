from .group_base_interpreter import *


def run(expr: EXPR, data_sources: dict, env: dict) -> list:
    """
    有 group 与 order 语句
    """
    # 执行 from 筛选
    data_sources = visit(expr.from_expr, data_sources, env)

    # 通过 select 语句先确定有哪些聚合函数，每一列的都需要新生成一个函数
    init_aggfuncs(expr.select_expr)

    # 排序规则
    env['order'] = tuple(get_desc_or_var(sub_expr) for sub_expr in expr.order_expr)

    data_sources, res = visit_group(expr, data_sources, env), []
    for pk, data_source in data_sources.items():
        condition_filter(expr, {pk: data_source}, res, env)

    # 如果有聚合函数
    if agg_position:
        agg_funcs.clear()
        agg_position.clear()
        try:
            if isinstance(res[-1], list):
                return [group_visit_select(expr.select_expr, res[-1][0], env)]
            else:
                return [group_visit_select(expr.select_expr, res[-1], env)]
        except IndexError:
            return []

    res = [
        group_visit_select(expr.select_expr, instance_dict, env)
        for instance_dict in res
    ]

    # limit 语句
    if expr.limit_expr:
        return visit_limit(expr.limit_expr, res, env)

    return res


def get_desc_or_var(expr):
    if isinstance(expr, VAR):
        return (0, *get_var(expr))
    return (1, *get_var(expr.args))


def condition_filter(expr: EXPR, instance_dict, res: list, env):
    if (not expr.having_expr) or expr.having_expr and group_visit(expr.having_expr, instance_dict, env):
        index = bisect_left(res, instance_dict, env.get('order'))
        res.insert(index, instance_dict)


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
    """
    item1/item2: {
        ('xxx', 'yyy'):
        [
            {
                'student': {'name': 'jay_chou', 'age': 40},
                'teacher': {'name': 'zzzz', 'year': 5}
            },
            {
                'student': {'name': 'jay_chou', 'age': 40},
                'teacher': {'name': 'zzzz', 'year': 5}
            }
        ]
    }
    """
    for order, table_name, attr in orders:
        for values in item1.values():
            for values2 in item2.values():
                v1 = values[0][table_name][attr]
                v2 = values2[0][table_name][attr]
                if v1 < v2:
                    return True if order == 0 else False
                if v1 > v2:
                    return False if order == 0 else True
                break
            break
    return True
