from collections import namedtuple
from typing import NewType

__all__ = ['SelectStatement', 'SQLToken', 'FROM', 'SELECT', 'VAR', 'CONST', 'UNKNOWN', 'STATES',
           'TABLES', 'AS', 'FUNC', 'CASE', 'INNER', 'OUTER', 'ORDER', 'DESC', 'LIMIT', 'LINK', 'EXPR']

# select 语句
SelectStatement = namedtuple('Root', ('id', 'tree'))
# 通用语句
SQLToken = namedtuple('Token', ('tag', 'args'))
# 子语句
FROM = namedtuple('from_expr', ('tables', 'condition', 'group', 'having'))
SELECT = namedtuple('select', ('from_expr', 'order', 'limit', 'select'))
VAR = namedtuple('var', ('name', 'attr', 'func'))
CONST = namedtuple('const', ('value',))
UNKNOWN = namedtuple('unknown', ())
# 语句集合
STATES = (FROM, SELECT, VAR, CONST, UNKNOWN)
# 节点标签
NODE = NewType('NODE', int)
TABLES = NODE(2)  # tables
AS = NODE(3)  # name, str
FUNC = NODE(4)  # name, *args
CASE = NODE(5)  # [*(condition, consequent)]
INNER = NODE(6)  # tableSourceItem
OUTER = NODE(7)  # tag, tableSourceItem, expression
ORDER = NODE(8)  # tuple(order_by_expressions)
DESC = NODE(9)  # expression
LIMIT = NODE(10)  # offset, limit
LINK = NODE(11)  # select_statement_id
# 结果列表
EXPR = namedtuple('sql_interpreter', (
    'from_expr',
    'where_expr',
    'group_expr',
    'having_expr',
    'order_expr',
    'limit_expr',
    'select_expr',
))
