from PyLinq.gen.MySqlParserVisitor import MySqlParserVisitor
from PyLinq.gen.MySqlParser import MySqlParser
from PyLinq.parser.nodes import *
from queue import Queue


class MySqlVisitor(MySqlParserVisitor):
    def __init__(self):
        """
        select_statements: 存放子 select 语句的队列，先入队的先执行
        get_id: 生成子 select 语句的 id
        """
        self.select_statements_queue = Queue()
        # get_id 方法用来获取一个递增的 id
        _id = [-1]
        self.get_id = lambda: [_id[0] for _id[0] in [_id[0]+1]][0]

    def visitQueryExpression(self, ctx: MySqlParser.QueryExpressionContext) -> SQLToken:
        """
        LR_BRACKET querySpecification RR_BRACKET | LR_BRACKET queryExpression RR_BRACKET
        """
        query_specification = ctx.querySpecification()
        if query_specification is None:
            query_expression = ctx.queryExpression()
            if query_expression:
                query_specification = self.visit(query_expression)
            else:
                query_specification = None
        else:
            query_specification = self.visit(query_specification)
        return query_specification

    def visitQuerySpecification(self, ctx: MySqlParser.QuerySpecificationContext) -> SQLToken:
        """ 每个 select 子句都需要入队
        SELECT DISTINCT? selectElements
        fromClause? orderByClause? limitClause?
        """
        distinct = True if ctx.DISTINCT() else False
        select_elements = self.visit(ctx.selectElements())
        from_clause = ctx.fromClause()
        from_clause = FROM(*self.visit(from_clause)) if from_clause else None
        order_by_clause = ctx.orderByClause()
        order_by_clause = self.visit(order_by_clause) if order_by_clause else None
        limit_clause = ctx.limitClause()
        limit_clause = self.visit(limit_clause) if limit_clause else None

        sql_token = SELECT(from_clause, order_by_clause, limit_clause, (distinct, *select_elements))
        tree = SelectStatement(self.get_id(), sql_token)
        self.select_statements_queue.put(tree)
        return SQLToken(LINK, tree.id)

    def visitSelectColumnElement(self, ctx: MySqlParser.SelectColumnElementContext) -> SQLToken:
        """
        fullColumnName (AS? ID)?
        """
        name = self.visit(ctx.fullColumnName())
        alis = ctx.ID()
        return SQLToken(AS, (name, CONST(alis.getText()))) if alis else name

    def visitSelectFunctionElement(self, ctx: MySqlParser.SelectFunctionElementContext) -> SQLToken:
        """
        functionCall (AS? ID)?
        """
        name = self.visit(ctx.functionCall())
        alis = ctx.ID()
        return SQLToken(AS, (name, CONST(alis.getText()))) if alis else name

    def visitSelectExpressionElement(self, ctx: MySqlParser.SelectExpressionElementContext) -> SQLToken:
        """
        expression (AS? ID)?
        """
        name = self.visit(ctx.expression())
        alis = ctx.ID()
        return SQLToken(AS, (name, CONST(alis.getText()))) if alis else name

    def visitSelectElements(self, ctx: MySqlParser.SelectElementsContext) -> SQLToken:
        """
        (star='*' | selectElement ) (',' selectElement)*
        """
        select_elements = [True if ctx.STAR() else False]
        for element in ctx.selectElement():
            select_elements.append(self.visit(element))
        return select_elements

    def visitFromClause(self, ctx: MySqlParser.FromClauseContext) -> SQLToken:
        """
        FROM tableSources
        (WHERE whereExpr=expression)?
        (
          GROUP BY
          groupByItem (',' groupByItem)*
          (HAVING havingExpr=expression)?
        )?
        """
        table_sources = self.visit(ctx.tableSources())
        group_expr = tuple(self.visit(item) for item in ctx.groupByItem()) if ctx.GROUP() else None
        if ctx.WHERE():
            where_expr = self.visit(ctx.expression(0))
            having_expr = self.visit(ctx.expression(1)) if ctx.HAVING() else None
            return table_sources, where_expr, group_expr, having_expr
        having_expr = self.visit(ctx.expression(0)) if ctx.HAVING() else None
        return table_sources, None, group_expr, having_expr

    def visitGroupByItem(self, ctx: MySqlParser.GroupByItemContext) -> SQLToken:
        """
        expression order=(ASC | DESC)?
        """
        return SQLToken(DESC, self.visit(ctx.expression())) if ctx.DESC() else self.visit(ctx.expression())

    def visitTableSourceBase(self, ctx: MySqlParser.TableSourceBaseContext) -> SQLToken:
        """
        tableSourceItem joinPart*
        """
        table_source_items = [self.visit(ctx.tableSourceItem())]
        for join_part in ctx.joinPart():
            table_source_items.append(self.visit(join_part))
        # return TABLES(table_source_items)
        return SQLToken(TABLES, table_source_items)

    def visitFunctionArgs(self, ctx: MySqlParser.FunctionArgsContext) -> SQLToken:
        """
        ('*' | ALL | constant | fullColumnName | functionCall | expression)
        (
          ','
          ('*' | ALL | constant | fullColumnName | functionCall | expression)
        )*
        """
        res = []
        for children in ctx.children:
            if children.getText() in ('*', 'ALL'):
                res.append(CONST('*'))
            else:
                val = self.visit(children)
                if val is not None:
                    res.append(val)
        return tuple(res)

    def visitTableSourceNested(self, ctx: MySqlParser.TableSourceNestedContext) -> SQLToken:
        """
        '(' tableSourceItem joinPart* ')'
        """
        table_source_items = [self.visit(ctx.tableSourceItem())]
        for join_part in ctx.joinPart():
            table_source_items.append(self.visit(join_part))
        # return TABLES(table_source_items)
        return SQLToken(TABLES, table_source_items)

    def visitInnerJoin(self, ctx: MySqlParser.InnerJoinContext) -> SQLToken:
        """
        (INNER | CROSS)? JOIN tableSourceItem
        """
        return SQLToken(INNER, self.visit(ctx.tableSourceItem()))

    def visitOuterJoin(self, ctx: MySqlParser.OuterJoinContext) -> SQLToken:
        """
        (LEFT | RIGHT) OUTER? JOIN tableSourceItem
        (
          ON expression
          | USING '(' uidList ')'
        )
        """
        if ctx.LEFT():
            expression = ctx.expression()
            if expression:
                return SQLToken(OUTER, ('left_on', self.visit(ctx.tableSourceItem()), self.visit(expression)))
            return SQLToken(OUTER, ('left_using', self.visit(ctx.tableSourceItem()), self.visit(ctx.uidList())))
        else:
            expression = ctx.expression()
            if expression:
                return SQLToken(OUTER, ('right_on', self.visit(ctx.tableSourceItem()), self.visit(expression)))
            return SQLToken(OUTER, ('right_using', self.visit(ctx.tableSourceItem()), self.visit(ctx.uidList())))

    def visitAtomTableItem(self, ctx: MySqlParser.AtomTableItemContext) -> SQLToken:
        """
        fullId (AS? alias=ID)?
        """
        name = self.visit(ctx.fullId())
        alis = ctx.ID()
        return SQLToken(AS, (name, CONST(alis.getText()))) if alis else name

    def visitFullId(self, ctx: MySqlParser.FullIdContext) -> SQLToken:
        """
        ID DOT_ID?
        """
        name = ctx.ID().getText()
        dot_id = ctx.DOT_ID()
        if dot_id:
            return VAR(CONST(name), CONST(dot_id.getText()[1:]), None)
        else:
            return VAR(CONST(name), None, None)

    def visitSubqueryTableItem(self, ctx: MySqlParser.SubqueryTableItemContext) -> SQLToken:
        """
        (
        selectStatement
        | '(' parenthesisSubquery=selectStatement ')'
        )
        AS? alias=ID
        """
        return SQLToken(AS, (self.visit(ctx.selectStatement()), CONST(ctx.ID().getText())))

    def visitTableSourcesItem(self, ctx: MySqlParser.TableSourcesItemContext) -> SQLToken:
        """
        '(' tableSources ')'
        """
        return self.visit(ctx.tableSources())

    def visitTableSources(self, ctx: MySqlParser.TableSourcesContext) -> SQLToken:
        """
        tableSource (',' tableSource)*
        """
        table_sources = ctx.tableSource()
        first_source = self.visit(table_sources[0])
        for table_source in table_sources[1:]:
            first_source.args.extend(self.visit(table_source).args)
        return first_source

    def visitOrderByClause(self, ctx: MySqlParser.OrderByClauseContext) -> SQLToken:
        """
        ORDER BY orderByExpression (',' orderByExpression)*
        """
        # order_by_expressions = tuple(self.visit(expression) for expression in ctx.orderByExpression())
        # return SQLToken(ORDER, order_by_expressions)
        return tuple(self.visit(expression) for expression in ctx.orderByExpression())

    def visitOrderByExpression(self, ctx: MySqlParser.OrderByExpressionContext) -> SQLToken:
        """
        expression order=(ASC | DESC)?
        """
        return SQLToken(DESC, self.visit(ctx.expression())) if ctx.DESC() else self.visit(ctx.expression())

    def visitLimitClause(self, ctx: MySqlParser.LimitClauseContext) -> SQLToken:
        """
        LIMIT
        (
          (offset=DECIMAL_LITERAL ',')? limit=DECIMAL_LITERAL
          | limit=DECIMAL_LITERAL OFFSET offset=DECIMAL_LITERAL
        )
        """
        if ctx.OFFSET():
            offset, limit = CONST(int(ctx.DECIMAL_LITERAL(1).getText())), CONST(int(ctx.DECIMAL_LITERAL(0).getText()))
        elif ctx.COMMA():
            offset, limit = CONST(int(ctx.DECIMAL_LITERAL(0).getText())), CONST(int(ctx.DECIMAL_LITERAL(1).getText()))
        else:
            offset, limit = CONST(0), CONST(int(ctx.DECIMAL_LITERAL(0).getText()))
        return SQLToken(LIMIT, (offset, limit))

    def visitNotExpression(self, ctx: MySqlParser.NotExpressionContext) -> SQLToken:
        """
        notOperator=(NOT | '!') expression
        """
        where_node = self.visit(ctx.expression())
        return SQLToken(FUNC, ('not', where_node))

    def visitLogicalExpression(self, ctx: MySqlParser.LogicalExpressionContext) -> SQLToken:
        """
        expression logicalOperator expression
        """
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return SQLToken(FUNC, (self.visit(ctx.logicalOperator()), left, right))

    def visitIsExpression(self, ctx: MySqlParser.IsExpressionContext) -> SQLToken:
        """
        predicate IS NOT? testValue=(TRUE | FALSE | UNKNOWN)
        """
        left = self.visit(ctx.predicate())
        val = ctx.testValue.text
        if ctx.NOT():
            if val == 'TRUE':
                return SQLToken(FUNC, ('is_not', left, CONST(True)))
            elif val == 'FALSE':
                return SQLToken(FUNC, ('is_not', left, CONST(False)))
            return SQLToken(FUNC, ('is_not', left, UNKNOWN()))
        if val == 'TRUE':
            return SQLToken(FUNC, ('is', left, CONST(True)))
        elif val == 'FALSE':
            return SQLToken(FUNC, ('is', left, CONST(False)))
        return SQLToken(FUNC, ('is', left, UNKNOWN()))

    def visitInPredicate(self, ctx: MySqlParser.InPredicateContext) -> SQLToken:
        """
        predicate NOT? IN '(' (selectStatement | expressions) ')':
        """
        left = self.visit(ctx.predicate())
        if ctx.NOT():
            select_statement = ctx.selectStatement()
            if select_statement:
                return SQLToken(FUNC, ('not_in', left, self.visit(select_statement)))
            else:
                return SQLToken(FUNC, ('not_in', left, self.visit(ctx.expressions())))
        select_statement = ctx.selectStatement()
        if select_statement:
            return SQLToken(FUNC, ('in', left, self.visit(select_statement)))
        else:
            return SQLToken(FUNC, ('in', left, self.visit(ctx.expressions())))

    def visitExpressions(self, ctx: MySqlParser.ExpressionsContext) -> tuple:
        """
        expression (',' expression)*
        """
        return tuple(self.visit(expression) for expression in ctx.expression())

    def visitIsNullPredicate(self, ctx: MySqlParser.IsNullPredicateContext) -> SQLToken:
        """
        predicate IS nullNotnull
        """
        left = self.visit(ctx.predicate())
        right = self.visit(ctx.nullNotnull())
        return SQLToken(FUNC, ('is', left, right))

    def visitNullNotnull(self, ctx: MySqlParser.NullNotnullContext) -> SQLToken:
        """
        NOT? (NULL_LITERAL | NULL_SPEC_LITERAL)
        """
        if ctx.NULL_LITERAL():
            return SQLToken(FUNC, ('not', CONST(None))) if ctx.NOT() else CONST(None)
        return SQLToken(FUNC, ('not', CONST('\n'))) if ctx.NOT() else CONST('\n')
        # return SQLToken(FUNC, ('not', '\n'), []) if ctx.NOT() else SQLToken(STR, '\n', [])

    def visitBinaryComparasionPredicate(self, ctx: MySqlParser.BinaryComparasionPredicateContext) -> SQLToken:
        """
        left=predicate comparisonOperator right=predicate
        """
        left = self.visit(ctx.predicate(0))
        op = self.visit(ctx.comparisonOperator())
        right = self.visit(ctx.predicate(1))
        return SQLToken(FUNC, (op, left, right))

    def visitComparisonOperator(self, ctx: MySqlParser.ComparisonOperatorContext) -> str:
        """
        '=' | '>' | '<' | '<' '=' | '>' '='
        | '<' '>' | '!' '=' | '<' '=' '>'
        """
        equal_symbol = ctx.EQUAL_SYMBOL()
        greter_symbol = ctx.GREATER_SYMBOL()
        less_symbol = ctx.LESS_SYMBOL()
        exclamation_symbol = ctx.EXCLAMATION_SYMBOL()
        if equal_symbol:
            if not less_symbol:
                if not exclamation_symbol:
                    if not greter_symbol:
                        return '='
                    else:
                        return '>='
                else:
                    return '!='
            else:
                if not greter_symbol:
                    return '<=>'
                else:
                    return '<='
        elif greter_symbol:
            if less_symbol:
                return '<>'
            else:
                return '>'
        elif less_symbol:
            return '<'

    def visitSubqueryComparasionPredicate(self, ctx: MySqlParser.SubqueryComparasionPredicateContext) -> SQLToken:
        """
        predicate comparisonOperator quantifier=(ALL | ANY | SOME) '(' selectStatement ')'
        """
        left = self.visit(ctx.predicate())
        op = self.visit(ctx.comparisonOperator())
        select_statement = self.visit(ctx.selectStatement())
        return SQLToken(FUNC, (ctx.quantifier.text + op, left, select_statement.id))

    def visitBetweenPredicate(self, ctx: MySqlParser.BetweenPredicateContext) -> SQLToken:
        """
        predicate NOT? BETWEEN predicate AND predicate
        """
        left = self.visit(ctx.predicate(0))
        start = self.visit(ctx.predicate(1))
        end = self.visit(ctx.predicate(2))
        if ctx.NOT():
            return SQLToken(FUNC, ('not_between', left, start, end))
        return SQLToken(FUNC, ('between', left, start, end))

    def visitLikePredicate(self, ctx: MySqlParser.LikePredicateContext) -> SQLToken:
        """
        predicate NOT? LIKE predicate
        """
        left = self.visit(ctx.predicate(0))
        right = self.visit(ctx.predicate(1))
        if ctx.NOT():
            return SQLToken(FUNC, ('not_like', left, right))
        return SQLToken(FUNC, ('like', left, right))

    def visitRegexpPredicate(self, ctx: MySqlParser.RegexpPredicateContext) -> SQLToken:
        """
        predicate NOT? regex=(REGEXP | RLIKE) predicate
        """
        left = self.visit(ctx.predicate(0))
        right = self.visit(ctx.predicate(1))
        if ctx.NOT():
            return SQLToken(FUNC, ('not_regexp', left, right))
        return SQLToken(FUNC, ('regexp', left, right))

    def visitConstant(self, ctx: MySqlParser.ConstantContext) -> SQLToken:
        """
        STRING_LITERAL | DECIMAL_LITERAL
        | '-' DECIMAL_LITERAL
        | booleanLiteral
        | REAL_LITERAL
        | NOT? nullLiteral=(NULL_LITERAL | NULL_SPEC_LITERAL)
        """
        string = ctx.STRING_LITERAL()
        if string:
            return CONST(string.getText()[1:-1])
        decimal = ctx.DECIMAL_LITERAL()
        minus = ctx.MINUS()
        if decimal:
            value = -1 * int(decimal.getText()) if minus else int(decimal.getText())
            return CONST(value)
        boolean = ctx.booleanLiteral()
        if boolean:
            value = self.visit(boolean)
            return value
        real = ctx.REAL_LITERAL()
        if real:
            value = float(real.getText())
            return CONST(value)
        if ctx.NOT():
            if ctx.NULL_LITERAL():
                return SQLToken(FUNC, ('not', CONST(None)))
            else:
                return CONST('\n')
        if ctx.NULL_LITERAL():
            return CONST(None)
        else:
            return CONST('\n')

    def visitBooleanLiteral(self, ctx: MySqlParser.BooleanLiteralContext) -> bool:
        return CONST(True) if ctx.TRUE() else CONST(False)

    def visitFullColumnName(self, ctx: MySqlParser.FullColumnNameContext) -> SQLToken:
        """
        ID (DOT_ID DOT_ID? )?
        """
        name = ctx.ID().getText()
        attr = ctx.DOT_ID(0)
        if attr:
            func = ctx.DOT_ID(1)
            attr = attr.getText()
            if func:
                func = func.getText()
                return VAR(CONST(name), CONST(attr[1:]), CONST(func[1:]))
            else:
                return VAR(CONST(name), CONST(attr[1:]), None)
        else:
            return VAR(name, None, None)

    def visitCaseFunctionCall(self, ctx: MySqlParser.CaseFunctionCallContext) -> SQLToken:
        """
        CASE caseFuncAlternative+
        (ELSE elseArg=functionArg)? END
        """
        branches = []
        for func_alternative in ctx.caseFuncAlternative():
            branches.append(self.visit(func_alternative))
        if ctx.ELSE():
            branches.append((None, self.visit(ctx.functionArg())))
        return SQLToken(CASE, branches)

    def visitCaseFuncAlternative(self, ctx: MySqlParser.CaseFuncAlternativeContext) -> tuple:
        """
        WHEN condition=functionArg
        THEN consequent=functionArg
        """
        return self.visit(ctx.functionArg(0)), self.visit(ctx.functionArg(1))

    def visitScalarFunctionCall(self, ctx: MySqlParser.ScalarFunctionCallContext) -> SQLToken:
        """
        ID '(' functionArgs? ')'
        """
        func_name = ctx.ID().getText()
        func_args = ctx.functionArgs()
        if func_args:
            func_args = self.visit(func_args)
            return SQLToken(FUNC, (func_name.lower(), *func_args))
        return SQLToken(FUNC, (func_name.lower(),))

    def visitUnaryExpressionAtom(self, ctx: MySqlParser.UnaryExpressionAtomContext) -> SQLToken:
        """
        unaryOperator expressionAtom
        """
        expression_atom = self.visit(ctx.expressionAtom())
        op = self.visit(ctx.unaryOperator())
        return SQLToken(FUNC, (op, expression_atom))

    def visitUnaryOperator(self, ctx: MySqlParser.UnaryOperatorContext) -> str:
        if ctx.NOT():
            return 'signal_not'
        return 'signal_' + self.visitChildren(ctx).getText()

    def visitNestedExpressionAtom(self, ctx: MySqlParser.NestedExpressionAtomContext) -> SQLToken:
        """
        '(' expression (',' expression)* ')'
        """
        return tuple(self.visit(item) for item in ctx.expression())

    def visitExistsExpressionAtom(self, ctx: MySqlParser.ExistsExpressionAtomContext) -> SQLToken:
        """
        EXISTS '(' selectStatement ')'
        """
        select_statement = self.visit(ctx.selectStatement())
        return SQLToken(FUNC, ('exits', select_statement))

    def visitMathExpressionAtom(self, ctx: MySqlParser.MathExpressionAtomContext) -> SQLToken:
        """
        left=expressionAtom mathOperator right=expressionAtom
        """
        left = self.visit(ctx.expressionAtom(0))
        right = self.visit(ctx.expressionAtom(1))
        return SQLToken(FUNC, (self.visit(ctx.mathOperator()), left, right))

    def visitMathOperator(self, ctx: MySqlParser.MathOperatorContext) -> str:
        """
        '*' | '/' | '%' | DIV | MOD | '+' | '-' | '--'
        """
        if ctx.DIV():
            return 'div'
        if ctx.MOD():
            return 'mod'
        return ctx.children[0].getText()

    def visitLogicalOperator(self, ctx: MySqlParser.LogicalOperatorContext) -> str:
        """
        AND | OR
        """
        return 'and' if ctx.AND() else 'or'
