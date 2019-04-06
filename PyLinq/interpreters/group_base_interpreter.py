from copy import deepcopy
from .common_interpreter import *


def get_groups(expr):
    return set(get_var(sub_expr) for sub_expr in expr)


def get_var(var_expr: VAR):
    return visit(var_expr.name, None, None), visit(var_expr.attr, None, None)


def visit_group(expr, data_sources, env):
    groups = get_groups(expr.group_expr)
    env['groups'] = groups
    res_dict = {}
    for instance_dict in main_loop(data_sources, {}, expr.where_expr, env):
        pk = tuple(instance_dict[table_name][attr] for table_name, attr in groups)
        res_dict.setdefault(pk, []).append(instance_dict)
    return res_dict


def main_loop(data_sources: dict, instance_dict, where_expr, env):
    name, instances = data_sources.popitem()
    for instance in instances:
        instance_dict[name] = instance
        # 如果是最后一张表,处理一行,否则取出下一张表
        if not data_sources:
            if where_expr:
                if visit(where_expr, instance_dict, env):
                    yield deepcopy(instance_dict)
            else:
                yield deepcopy(instance_dict)
        else:
            for res in main_loop(data_sources.copy(), instance_dict, where_expr, env):
                yield res
        # 处理完将本条记录删除
        del instance_dict[name]


def group_visit_select(select_expr: tuple, instance_dict, env) -> dict:
    """
    :param instance_dict:
    :param env:
    :param select_expr:
    {
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
    :return:
    """
    res = {}
    # * 表达式
    if select_expr[1]:
        for values in instance_dict.keys():
            instances = values[0]
            for instance in instances.values():
                for key, value in instance.items():
                    res[key] = value
            return res

    for i, expr in enumerate(select_expr[2:]):
        # 不存在聚合函数
        if not agg_position:
            key, value = make_name(expr, group_visit(expr, instance_dict, env))
            res[key] = value[-1] if isinstance(value, (list, tuple)) else value
        elif isinstance(expr, SQLToken) and expr.tag == FUNC:
            res = make_name(expr, group_visit(expr, instance_dict, env, i))
        else:
            key, value = make_name(expr, group_visit(expr, instance_dict, env, i))
            res[key] = value[-1] if isinstance(value, (list, tuple)) else value
    return res


def group_visit_as(as_expr: SQLToken, data_sources, env, index) -> tuple:
    """
    :param as_expr:
    :param data_sources:
    :param env:
    :param index: {
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
    :return:
    """
    new_name = group_visit(as_expr.args[1], data_sources, env, index)
    return new_name, group_visit(as_expr.args[0], data_sources, env, index)


def group_visit_var(var_expr: VAR, data_sources: dict, env: dict, index):
    """
    {
        ('xxx', 'yyy'):
        [
            {
                'student': {'name': 'jay_chou', 'age': 40},
                'teacher': {'id': 'zzzz', 'year': 5}
            },
            {
                'student': {'name': 'jay_chow', 'age': 30},
                'teacher': {'id': 'xxxx', 'year': 6}
            }
        ]
    } + student.name -> ['jay_chou', 'jay_chow']
    """
    name = visit(var_expr.name, data_sources, env, index)
    attr = visit(var_expr.attr, data_sources, env, index)
    func = visit(var_expr.func, data_sources, env, index)
    value = []
    for values in data_sources.values():
        for instance_dict in values:
            if (name, attr) in env.get('groups'):
                return FuncProxy.get(func)(instance_dict[name][attr]) if func else instance_dict[name][attr]
            value.append(instance_dict[name][attr])
        return FuncProxy.get(func)(value) if func else value


def group_func_star(data_sources):
    """
    {
        ('xxx', 'yyy'):
        [
            {
                'student': {'name': 'jay_chou', 'age': 40},
                'teacher': {'id': 'zzzz', 'year': 5}
            },
            {
                'student': {'name': 'jay_chow', 'age': 30},
                'teacher': {'id': 'xxxx', 'year': 6}
            }
        ]
    } -> (
        ['jay_chou', 'jay_chow'],
        [40, 30],
        ['zzzz', 'xxxx'],
        [5, 6]
    )
    """
    res = []
    for values in data_sources.values():
        l = len(values)
        instance_dict = values[0]
        for table_name, line in instance_dict.items():
            for column_name, v in line.items():
                row = [v]
                i = 0
                while i + 1 < l:
                    instance_dict2 = values[i+1]
                    row.append(instance_dict2[table_name][column_name])
                    i += 1
                res.append(row)
        return tuple(res)


def group_visit_func(func_expr: SQLToken, data_sources, env, index):
    """
    :param func_expr:
    :param data_sources: {
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
    :param env:
    :param index:
    :return:
    """
    name = func_expr.args[0]

    if index is not None and index in agg_position:
        func = agg_funcs.get(name + str(index))
        if func is None:
            func = FuncProxy.get(name)
    else:
        func = FuncProxy.get(name)

    args = []
    for arg in func_expr.args[1:]:
        arg = group_visit(arg, data_sources, env, index)
        if arg == '*':
            args.extend(group_func_star(data_sources))
        else:
            args.append(arg)
    return func(*args)


def group_visit_case(case_expr: SQLToken, data_sources: dict, env, index):
    for condition, value in case_expr.args:
        if condition is None or group_visit(condition, data_sources, env, index):
            return group_visit(value, data_sources, env, index)


def group_visit(sql_expr, data_sources, env, index=None):
    if sql_expr is None:
        return None
    if isinstance(sql_expr, STATES):
        return group_visit_dict[sql_expr.__class__](sql_expr, data_sources, env, index)
    if isinstance(sql_expr, SQLToken):
        return group_visit_dict[sql_expr.tag](sql_expr, data_sources, env, index)
    if isinstance(sql_expr, (list, tuple, set)):
        return (group_visit(sub_expr, data_sources, env, index) for sub_expr in sql_expr)


group_visit_dict = {
    VAR: group_visit_var,
    CONST: visit_const,
    AS: group_visit_as,
    FUNC: group_visit_func,
    LINK: visit_link,
    CASE: group_visit_case,
}

