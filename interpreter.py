from nodes import *
from proxy import FuncProxy


agg_funcs = dict()


def _compare(orders: list, item: dict, other: dict, gt: bool) -> bool:
    for order, table_name, attr in orders:
        v1 = item[table_name][other]
        v2 = other[table_name][other]
        if v1 > v2:
            if gt:
                return True if order == 0 else False
            else:
                return False if order == 0 else True
        if v1 <= v2:
            if gt:
                return False if order == 0 else True
            else:
                return True if order == 0 else False


class QuerySet:
    def __init__(self, group_expr, order_expr, select_expr):
        """
        res 存放结果数据
        ids 给 group 分组用，存放主键
        length 结果长度
        group [
            [0, table_name, attr],  # 第一个参数: 0正序,1倒叙 第二个参数: 表名 第三个参数: 表字段
            [1, table_name, attr],  # 例如 [0, 'Teacher', 'name'] 意味按照 'Teacher' 表的 'name' 字段正序排列, 并分组
            [0, table_name, attr]   # 按顺序比较, 先比较前面的, 如果相等再比较后面的。
        ]
        order [
            [0, table_name, attr],  # 第一个参数: 0正序,1倒叙 第二个参数: 表名 第三个参数: 表字段
            [1, table_name, attr],  # 例如 [0, 'Teacher', 'name'] 意味按照 'Teacher' 表的 'name' 字段正序排列,
            [0, table_name, attr]   # 按顺序比较, 先比较前面的, 如果相等再比较后面的。
        ]
        select (
            distinct,  # 是否分组，暂不支持！！！！！！，bool
            star,      # `*` 表达式表示全选，bool
            *args      # 其他参数，例如函数、字段名等
        )
        """
        self.res = []
        self.ids = set()
        self.length = 0
        self.group = [get_expr(sub_group) for sub_group in group_expr]
        self.order = [get_expr(sub_order) for sub_order in order_expr]
        self.select = select_expr
        for expr in select_expr[2:]:
            if isinstance(expr, SQLToken) and expr.tag == AGGFUNC:
                agg_funcs[expr.args[0]] = FuncProxy.get(expr.args[0])

    def _gt(self, item, other) -> bool:
        """
        other/item: {
            'student': {'name': 'jay_chou', 'age': 40},
            'teacher': {'name': 'zzzz', 'year': 5}
        } 这样的数据, 每一张表只取一行, 凑成的一条数据
        """
        if self.order:
            return _compare(self.order, item, other, True)
        else:
            return _compare(self.group, item, other, True)

    def _lte(self, item, other) -> bool:
        """
        other/item: {
            'student': {'name': 'jay_chou', 'age': 40},
            'teacher': {'name': 'zzzz', 'year': 5}
        } 这样的数据, 每一张表只取一行, 凑成的一条数据
        """
        if self.order:
            return _compare(self.order, item, other, False)
        else:
            return _compare(self.group, item, other, False)

    def _append(self, item, start, end):
        """ 二分法插入数据
        item: {
            'student': {'name': 'jay_chou', 'age': 40},
            'teacher': {'name': 'zzzz', 'year': 5}
        } 这样的数据, 每一张表只取一行, 凑成的一条数据
        """
        if start == end:
            if self._lte(self.res[start], item):
                if start == self.length:
                    self.res.append(visit(self.select, item))
                else:
                    self.res.insert(start+1, visit(self.select, item))
            else:
                self.res.insert(start-1, visit(self.select, item))
        mid = (start + end) // 2
        if self._gt(self.res[mid], item) and self._lte(self.res[mid-1], item):
            self.res.append(visit(self.select, item))
        elif self._gt(self.res[mid-1], item):
            self._append(item, start, mid - 1)
        elif self._lte(self.res[mid], item):
            self._append(item, mid, end)

    def append(self, item):
        """
        item: {
            'student': {'name': 'jay_chou', 'age': 40},
            'teacher': {'name': 'zzzz', 'year': 5}
        } 这样的数据, 每一张表只取一行, 凑成的一条数据
        """
        if not self.group:
            if self.order:
                self._append(item, 0, self.length)
            else:
                self.res.append(item)
            self.length += 1
        else:
            pk = tuple(item[table_name][attr] for order, table_name, attr in self.group)
            if pk not in self.ids:
                self.ids.add(pk)
                if self.order:
                    self._append(item, 0, self.length)
                else:
                    self._append(item, 0, self.length)
                self.length += 1


def get_expr(expr):
    """
    只用来获取语句的参数
    """
    if expr is None:
        return None
    if isinstance(expr, SQLToken):
        return get_expr_dict[expr.tag](expr)
    return get_expr_dict[expr.__dict__.__name__.lower()](expr)


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
        return attr, FuncProxy.get(func)(value) if func else attr, value
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
    else:
        for expr in select_expr[2:]:
            if isinstance(expr, SQLToken) and expr.tag == FUNC:
                res[expr.args[0]] = visit(expr, data_sources)
            else:
                key, value = visit(expr, data_sources)
                res[key] = value
        return res


def visit_as(as_expr: SQLToken, data_sources) -> tuple:
    """
    :param as_expr:
    :param data_sources: {
        'student': {'name': 'jay_chou', 'age': 40},
        'teacher': {'name': 'zzzz', 'year': 5}
    } 这样的数据, 每一张表只取一行, 凑成的一条数据
    :return:
    """
    res = visit(as_expr.args[0], data_sources)
    rename = visit(as_expr.args[1], data_sources)
    return rename, res[1]


def visit_func(func_expr: SQLToken, data_sources):
    func = FuncProxy.get(func_expr.args[0])
    return func(*[visit(arg, data_sources) for arg in func_expr.args[1:]])


def visit_aggfunc(aggfunc_expr: SQLToken, data_sources):
    func = agg_funcs[aggfunc_expr.tag]
    return func(*[visit(arg, data_sources) for arg in aggfunc_expr.args[1:]])


def visit_limit(limit_expr: SQLToken, res: list) -> list:
    offset, limit = visit(limit_expr.args[0], res), visit(limit_expr.args[1], res)
    return res[offset:offset+limit]


def visit(sql_expr, data_sources):
    if sql_expr is None:
        return None
    if isinstance(sql_expr, STATES):
        tag_visit_dict[sql_expr.__dict__.__name__.lower()](sql_expr, data_sources)
    if isinstance(sql_expr, SQLToken):
        return tag_visit_dict[sql_expr.tag](sql_expr, data_sources)
    if isinstance(sql_expr, (list, tuple, set)):
        return (visit(sub_expr, data_sources) for sub_expr in sql_expr)


tag_visit_dict = {
    TABLES: visit_tables,
    VAR: visit_var,
    INNER: visit_inner,
    CONST: visit_const,
    SELECT: visit_select,
    AS: visit_as,
    FUNC: visit_func,
    LIMIT: visit_limit,
}

get_expr_dict = {
    VAR: get_var,
    CONST: visit_const,
    DESC: get_desc,
}


def main_loop(res_list: ResList, data_sources: dict, instance_dict, res: QuerySet) -> QuerySet:
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


def condition_filter(res_list: ResList, instance_dict, res: QuerySet) -> QuerySet:
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
                res.append(instance_dict)
        else:
            if visit(res_list.condition, instance_dict):
                res.append(instance_dict)
    else:
        res.append(instance_dict)
    return res


def sql_interpreter(sql_expr: SELECT, data_sources: dict) -> list:
    """
    入口
    :param sql_expr:
    :param data_sources:
    :return:
    """
    data_sources = visit(sql_expr.from_expr.tables, data_sources)
    from_expr = sql_expr.from_expr
    res_list = ResList([], from_expr.condition, from_expr.having)
    limit = sql_expr.limit

    res = main_loop(res_list, data_sources, {}, QuerySet(res_list.group_expr, res_list.order_expr, sql_expr.select)).res
    # 如果有聚合函数
    if agg_funcs:
        agg_funcs.clear()
        return [res[-1]]
    return visit(limit, res) if limit else res
