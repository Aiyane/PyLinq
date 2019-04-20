# Generated from /Users/zhangzhiqiang/PycharmProjects/PyLinq/PyLinq/parser/MySqlParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySqlParser import MySqlParser
else:
    from MySqlParser import MySqlParser

# This class defines a complete generic visitor for a parse tree produced by MySqlParser.

class MySqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySqlParser#simpleSelect.
    def visitSimpleSelect(self, ctx:MySqlParser.SimpleSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx:MySqlParser.ParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#orderByClause.
    def visitOrderByClause(self, ctx:MySqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#orderByExpression.
    def visitOrderByExpression(self, ctx:MySqlParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourceBase.
    def visitTableSourceBase(self, ctx:MySqlParser.TableSourceBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourceNested.
    def visitTableSourceNested(self, ctx:MySqlParser.TableSourceNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSources.
    def visitTableSources(self, ctx:MySqlParser.TableSourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#atomTableItem.
    def visitAtomTableItem(self, ctx:MySqlParser.AtomTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx:MySqlParser.SubqueryTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourcesItem.
    def visitTableSourcesItem(self, ctx:MySqlParser.TableSourcesItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#innerJoin.
    def visitInnerJoin(self, ctx:MySqlParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#outerJoin.
    def visitOuterJoin(self, ctx:MySqlParser.OuterJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryExpression.
    def visitQueryExpression(self, ctx:MySqlParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#querySpecification.
    def visitQuerySpecification(self, ctx:MySqlParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectElements.
    def visitSelectElements(self, ctx:MySqlParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:MySqlParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx:MySqlParser.SelectFunctionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx:MySqlParser.SelectExpressionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fromClause.
    def visitFromClause(self, ctx:MySqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#groupByItem.
    def visitGroupByItem(self, ctx:MySqlParser.GroupByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#limitClause.
    def visitLimitClause(self, ctx:MySqlParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullId.
    def visitFullId(self, ctx:MySqlParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullColumnName.
    def visitFullColumnName(self, ctx:MySqlParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:MySqlParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nullNotnull.
    def visitNullNotnull(self, ctx:MySqlParser.NullNotnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constant.
    def visitConstant(self, ctx:MySqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uidList.
    def visitUidList(self, ctx:MySqlParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressions.
    def visitExpressions(self, ctx:MySqlParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:MySqlParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:MySqlParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx:MySqlParser.CaseFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseFuncAlternative.
    def visitCaseFuncAlternative(self, ctx:MySqlParser.CaseFuncAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionArgs.
    def visitFunctionArgs(self, ctx:MySqlParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionArg.
    def visitFunctionArg(self, ctx:MySqlParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#isExpression.
    def visitIsExpression(self, ctx:MySqlParser.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#notExpression.
    def visitNotExpression(self, ctx:MySqlParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MySqlParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#predicateExpression.
    def visitPredicateExpression(self, ctx:MySqlParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:MySqlParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#inPredicate.
    def visitInPredicate(self, ctx:MySqlParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryComparasionPredicate.
    def visitSubqueryComparasionPredicate(self, ctx:MySqlParser.SubqueryComparasionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:MySqlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binaryComparasionPredicate.
    def visitBinaryComparasionPredicate(self, ctx:MySqlParser.BinaryComparasionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx:MySqlParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#likePredicate.
    def visitLikePredicate(self, ctx:MySqlParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx:MySqlParser.RegexpPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:MySqlParser.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryExpressionAtom.
    def visitSubqueryExpressionAtom(self, ctx:MySqlParser.SubqueryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#priorityMathExpressionAtom.
    def visitPriorityMathExpressionAtom(self, ctx:MySqlParser.PriorityMathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:MySqlParser.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:MySqlParser.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx:MySqlParser.FullColumnNameExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx:MySqlParser.NestedExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx:MySqlParser.MathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#existsExpressionAtom.
    def visitExistsExpressionAtom(self, ctx:MySqlParser.ExistsExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unaryOperator.
    def visitUnaryOperator(self, ctx:MySqlParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:MySqlParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#logicalOperator.
    def visitLogicalOperator(self, ctx:MySqlParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mathOperator.
    def visitMathOperator(self, ctx:MySqlParser.MathOperatorContext):
        return self.visitChildren(ctx)



del MySqlParser