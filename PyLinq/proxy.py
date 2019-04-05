import re
import logging


class FuncProxy:
    """
    代理 SQL 内建函数类。
    sql_funcs: 保存 sql 中函数名为 key，funcs 包中相应的闭包函数为 value。
    """
    aggr = set()
    sql_funcs = {
        'first': lambda: lambda x: x[0],
        'not': lambda: lambda x: not x,
        'signal_not': lambda: lambda x: not x,
        'signal_!': lambda: lambda x: not x,
        'signal_+': lambda: lambda x: x,
        'signal_-': lambda: lambda x: -1*x,
        '--': lambda: lambda x: x,
        'signal_~': lambda: lambda x: ~x,
        '+': lambda: lambda x, y: x + y,
        '-': lambda: lambda x, y: x - y,
        '*': lambda: lambda x, y: x * y,
        '/': lambda: lambda x, y: x / y,
        '%': lambda: lambda x, y: x % y,
        'exits': lambda: lambda x: any(x),
        'is': lambda: lambda x, y: x is y,
        'is_not': lambda: lambda x, y: x is not y,
        'in': lambda: lambda x, y: x in y,
        'not_in': lambda: lambda x, y: x not in y,
        'or': lambda: lambda x, y: x or y,
        'and': lambda: lambda x, y: x and y,
        '=': lambda: lambda x, y: x == y,
        '>=': lambda: lambda x, y: x >= y,
        '<=': lambda: lambda x, y: x <= y,
        '>': lambda: lambda x, y: x > y,
        '<': lambda: lambda x, y: x < y,
        '<>': lambda: lambda x, y: x != y,
        '!=': lambda: lambda x, y: x != y,
        '<=>': lambda: lambda x, y: x != y,
        'ALL=': lambda: lambda x, y: all((x == v for v in y)),
        'ALL>=': lambda: lambda x, y: all((x >= v for v in y)),
        'ALL<=': lambda: lambda x, y: all((x <= v for v in y)),
        'ALL>': lambda: lambda x, y: all((x > v for v in y)),
        'ALL<': lambda: lambda x, y: all((x < v for v in y)),
        'ALL<>': lambda: lambda x, y: all((x != v for v in y)),
        'ALL!=': lambda: lambda x, y: all((x != v for v in y)),
        'ALL<=>': lambda: lambda x, y: all((x != v for v in y)),
        'ANY=': lambda: lambda x, y: any((x == v for v in y)),
        'ANY>=': lambda: lambda x, y: any((x >= v for v in y)),
        'ANY<=': lambda: lambda x, y: any((x <= v for v in y)),
        'ANY>': lambda: lambda x, y: any((x > v for v in y)),
        'ANY<': lambda: lambda x, y: any((x < v for v in y)),
        'ANY<>': lambda: lambda x, y: any((x != v for v in y)),
        'ANY!=': lambda: lambda x, y: any((x != v for v in y)),
        'ANY<=>': lambda: lambda x, y: any((x != v for v in y)),
        'SOME=': lambda: lambda x, y: any((x == v for v in y)),
        'SOME>=': lambda: lambda x, y: any((x >= v for v in y)),
        'SOME<=': lambda: lambda x, y: any((x <= v for v in y)),
        'SOME>': lambda: lambda x, y: any((x > v for v in y)),
        'SOME<': lambda: lambda x, y: any((x < v for v in y)),
        'SOME<>': lambda: lambda x, y: any((x != v for v in y)),
        'SOME!=': lambda: lambda x, y: any((x != v for v in y)),
        'SOME<=>': lambda: lambda x, y: any((x != v for v in y)),
        'not_between': lambda: lambda x, s, e: x < s or x > e,
        'between': lambda: lambda x, s, e: s <= x <= e,
        'not_regexp': lambda: lambda x, y: re.match(y, x) is None,
        'regexp': lambda: lambda x, y: re.match(y, x) is not None,
        'like': lambda: lambda x, y: re.match(y.replace('.', '\\.').replace('^', '\\^').replace('$', '\\$').replace(
            '*', '\\*').replace('+', '\\+').replace('?', '\\?').replace('{', '\\{').replace('}', '\\}').replace(
            '\\', '\\\\').replace('|', '\\|').replace('(', '\\(').replace(')', '\\)').replace('%', '.*'), x) is not None,
        'not_like': lambda x, y: re.match(y.replace('.', '\\.').replace('^', '\\^').replace('$', '\\$').replace(
            '*', '\\*').replace('+', '\\+').replace('?', '\\?').replace('{', '\\{').replace('}', '\\}').replace(
            '\\', '\\\\').replace('|', '\\|').replace('(', '\\(').replace(')', '\\)').replace('%', '.*'), x) is None,
    }

    @classmethod
    def add(cls, name, func):
        if name in cls.sql_funcs:
            logging.error("%s as sql func repeatedly", name)
        FuncProxy.sql_funcs[name] = func

    @classmethod
    def get(cls, name):
        func = cls.sql_funcs.get(name, None)
        return None if func is None else func()
