from .common_interpreter import *


def run(expr: EXPR, data_sources: dict, env: dict) -> list:
    """
    无 group 语句
    """
    # 执行 from 筛选
    data_sources = visit(expr.from_expr, data_sources, env)
    # 通过 select 语句先确定有哪些聚合函数，每一列的都需要新生成一个函数
    init_aggfuncs(expr.select_expr)
    # 排序规则
    env['order'] = tuple(get_desc_or_var(sub_expr) for sub_expr in expr.order_expr)
    res = index_loop(expr, data_sources, env, []) if expr.index_expr else main_loop(expr, data_sources, {}, [], env)

    # 如果有聚合函数
    if agg_position:
        agg_funcs.clear()
        agg_position.clear()
        try:
            if isinstance(res[-1], list):
                return [visit_select(expr.select_expr, res[-1][0], env)]
            else:
                return [visit_select(expr.select_expr, res[-1], env)]
        except IndexError:
            return []

    res = [
        visit_select(expr.select_expr, instance_dict, env)
        for instance_dict in res
    ]

    # limit 语句
    if expr.limit_expr:
        return visit_limit(expr.limit_expr, res, env)

    return res


def get_var(var_expr: VAR):
    """
    :param var_expr:
    :return:
    """
    return visit(var_expr.name, None, None), visit(var_expr.attr, None, None)


def get_desc_or_var(expr):
    if isinstance(expr, VAR):
        return (0, *get_var(expr))
    return (1, *get_var(expr.args))


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
        index = bisect_left(res, instance_dict, env.get('order'))
        res.insert(index, instance_dict.copy())


def index_loop(expr, data_sources, env, res):
    for instance_dict in visit_index(expr, data_sources):
        if data_sources:
            main_loop(expr, data_sources.copy(), instance_dict, res, env)
        else:
            condition_filter(expr, instance_dict, res, env)
    return res


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
