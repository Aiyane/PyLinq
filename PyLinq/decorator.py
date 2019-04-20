from functools import wraps
from PyLinq.proxy import FuncProxy, QueueProxy


def register_func(alias, is_aggr=False):
    """
    注册内建函数的装饰器
    :param alias: SQL 中该函数名
    :param is_aggr: 是否为聚合函数
    :return:
    """
    def _func(func):
        func_name = alias.lower() or func.__name__.lower()
        FuncProxy.add(func_name, func)
        if is_aggr:
            FuncProxy.aggr.add(func_name)
    return _func


def queue_cache(func):
    """
    保存 sql 表达式对应的 语法树队列
    """
    @wraps(func)
    def __func(sql_expr: str):
        queues = QueueProxy.get(sql_expr)
        if queues:
            return queues

        queue = func(sql_expr)
        QueueProxy.add(sql_expr, queue)
        return queue
    return __func
