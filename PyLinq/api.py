from antlr4 import CommonTokenStream, InputStream

from gen.MySqlLexer import MySqlLexer
from gen.MySqlParser import MySqlParser

from PyLinq.interpreters import simple_interpreter, order_interpreter, group_interpreter, group_order_interpreter
from PyLinq.parser.visitor import MySqlVisitor
from PyLinq.parser.nodes import EXPR

__SQL_ENV__ = {}  # 运行环境


# @lru_cache(maxsize=128)
def get_sql_queue(sql_expr: str):
    """
    获取 SQL 语句构造的语法树队列
    """
    input_stream = InputStream(sql_expr)
    lexer = MySqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    visitor = MySqlVisitor()
    tree = parser.queryExpression()
    visitor.visit(tree)
    return visitor.select_statements_queue


def sql_run(sql_expr: str, data_sources: dict):
    """
    运行 SQL 语句接口
    :param sql_expr: SQL 语句字符串
    :param data_sources: 数据源
    :return: 结果列表
    """
    sql_queue = get_sql_queue(sql_expr)
    env = {}  # 运行环境

    while 1:
        sql_expr = sql_queue.get()
        tree = sql_expr.tree

        result = sql_interpreter(tree, data_sources, env)

        if sql_queue.empty():
            return result

        env[sql_expr.id] = result


def sql_interpreter(tree, data_sources: dict, env: dict) -> list:
    """
    解释器总入口
    :param env: 运行环境
    :param tree: 语法树
    :param data_sources: 数据源
    :return: 执行结果
    """
    front_part = tree.from_expr

    return select_sql_interpreter_exec(
        EXPR(
            front_part.tables,
            front_part.condition,
            front_part.group,
            front_part.having,
            tree.order,
            tree.limit,
            tree.select
        ),
        data_sources, env
    )


def select_sql_interpreter_exec(expr, data_sources, env) -> list:
    if expr.group_expr:
        if expr.order_expr:
            return group_order_interpreter.run(expr, data_sources, env)
        else:
            return group_interpreter.run(expr, data_sources, env)
    elif expr.order_expr:
        return order_interpreter.run(expr, data_sources, env)
    else:
        return simple_interpreter.run(expr, data_sources, env)
