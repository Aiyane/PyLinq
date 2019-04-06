# Generated from /Users/zhangzhiqiang/PycharmProjects/test/PyLinq/MySqlParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySqlParser import MySqlParser
else:
    from MySqlParser import MySqlParser

# This class defines a complete listener for a parse tree produced by MySqlParser.
class MySqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by MySqlParser#simpleSelect.
    def enterSimpleSelect(self, ctx:MySqlParser.SimpleSelectContext):
        pass

    # Exit a parse tree produced by MySqlParser#simpleSelect.
    def exitSimpleSelect(self, ctx:MySqlParser.SimpleSelectContext):
        pass


    # Enter a parse tree produced by MySqlParser#parenthesisSelect.
    def enterParenthesisSelect(self, ctx:MySqlParser.ParenthesisSelectContext):
        pass

    # Exit a parse tree produced by MySqlParser#parenthesisSelect.
    def exitParenthesisSelect(self, ctx:MySqlParser.ParenthesisSelectContext):
        pass


    # Enter a parse tree produced by MySqlParser#orderByClause.
    def enterOrderByClause(self, ctx:MySqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by MySqlParser#orderByClause.
    def exitOrderByClause(self, ctx:MySqlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by MySqlParser#orderByExpression.
    def enterOrderByExpression(self, ctx:MySqlParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by MySqlParser#orderByExpression.
    def exitOrderByExpression(self, ctx:MySqlParser.OrderByExpressionContext):
        pass


    # Enter a parse tree produced by MySqlParser#tableSourceBase.
    def enterTableSourceBase(self, ctx:MySqlParser.TableSourceBaseContext):
        pass

    # Exit a parse tree produced by MySqlParser#tableSourceBase.
    def exitTableSourceBase(self, ctx:MySqlParser.TableSourceBaseContext):
        pass


    # Enter a parse tree produced by MySqlParser#tableSourceNested.
    def enterTableSourceNested(self, ctx:MySqlParser.TableSourceNestedContext):
        pass

    # Exit a parse tree produced by MySqlParser#tableSourceNested.
    def exitTableSourceNested(self, ctx:MySqlParser.TableSourceNestedContext):
        pass


    # Enter a parse tree produced by MySqlParser#tableSources.
    def enterTableSources(self, ctx:MySqlParser.TableSourcesContext):
        pass

    # Exit a parse tree produced by MySqlParser#tableSources.
    def exitTableSources(self, ctx:MySqlParser.TableSourcesContext):
        pass


    # Enter a parse tree produced by MySqlParser#atomTableItem.
    def enterAtomTableItem(self, ctx:MySqlParser.AtomTableItemContext):
        pass

    # Exit a parse tree produced by MySqlParser#atomTableItem.
    def exitAtomTableItem(self, ctx:MySqlParser.AtomTableItemContext):
        pass


    # Enter a parse tree produced by MySqlParser#subqueryTableItem.
    def enterSubqueryTableItem(self, ctx:MySqlParser.SubqueryTableItemContext):
        pass

    # Exit a parse tree produced by MySqlParser#subqueryTableItem.
    def exitSubqueryTableItem(self, ctx:MySqlParser.SubqueryTableItemContext):
        pass


    # Enter a parse tree produced by MySqlParser#tableSourcesItem.
    def enterTableSourcesItem(self, ctx:MySqlParser.TableSourcesItemContext):
        pass

    # Exit a parse tree produced by MySqlParser#tableSourcesItem.
    def exitTableSourcesItem(self, ctx:MySqlParser.TableSourcesItemContext):
        pass


    # Enter a parse tree produced by MySqlParser#innerJoin.
    def enterInnerJoin(self, ctx:MySqlParser.InnerJoinContext):
        pass

    # Exit a parse tree produced by MySqlParser#innerJoin.
    def exitInnerJoin(self, ctx:MySqlParser.InnerJoinContext):
        pass


    # Enter a parse tree produced by MySqlParser#outerJoin.
    def enterOuterJoin(self, ctx:MySqlParser.OuterJoinContext):
        pass

    # Exit a parse tree produced by MySqlParser#outerJoin.
    def exitOuterJoin(self, ctx:MySqlParser.OuterJoinContext):
        pass


    # Enter a parse tree produced by MySqlParser#queryExpression.
    def enterQueryExpression(self, ctx:MySqlParser.QueryExpressionContext):
        pass

    # Exit a parse tree produced by MySqlParser#queryExpression.
    def exitQueryExpression(self, ctx:MySqlParser.QueryExpressionContext):
        pass


    # Enter a parse tree produced by MySqlParser#querySpecification.
    def enterQuerySpecification(self, ctx:MySqlParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by MySqlParser#querySpecification.
    def exitQuerySpecification(self, ctx:MySqlParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by MySqlParser#selectElements.
    def enterSelectElements(self, ctx:MySqlParser.SelectElementsContext):
        pass

    # Exit a parse tree produced by MySqlParser#selectElements.
    def exitSelectElements(self, ctx:MySqlParser.SelectElementsContext):
        pass


    # Enter a parse tree produced by MySqlParser#selectColumnElement.
    def enterSelectColumnElement(self, ctx:MySqlParser.SelectColumnElementContext):
        pass

    # Exit a parse tree produced by MySqlParser#selectColumnElement.
    def exitSelectColumnElement(self, ctx:MySqlParser.SelectColumnElementContext):
        pass


    # Enter a parse tree produced by MySqlParser#selectFunctionElement.
    def enterSelectFunctionElement(self, ctx:MySqlParser.SelectFunctionElementContext):
        pass

    # Exit a parse tree produced by MySqlParser#selectFunctionElement.
    def exitSelectFunctionElement(self, ctx:MySqlParser.SelectFunctionElementContext):
        pass


    # Enter a parse tree produced by MySqlParser#selectExpressionElement.
    def enterSelectExpressionElement(self, ctx:MySqlParser.SelectExpressionElementContext):
        pass

    # Exit a parse tree produced by MySqlParser#selectExpressionElement.
    def exitSelectExpressionElement(self, ctx:MySqlParser.SelectExpressionElementContext):
        pass


    # Enter a parse tree produced by MySqlParser#fromClause.
    def enterFromClause(self, ctx:MySqlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by MySqlParser#fromClause.
    def exitFromClause(self, ctx:MySqlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by MySqlParser#groupByItem.
    def enterGroupByItem(self, ctx:MySqlParser.GroupByItemContext):
        pass

    # Exit a parse tree produced by MySqlParser#groupByItem.
    def exitGroupByItem(self, ctx:MySqlParser.GroupByItemContext):
        pass


    # Enter a parse tree produced by MySqlParser#limitClause.
    def enterLimitClause(self, ctx:MySqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by MySqlParser#limitClause.
    def exitLimitClause(self, ctx:MySqlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by MySqlParser#fullId.
    def enterFullId(self, ctx:MySqlParser.FullIdContext):
        pass

    # Exit a parse tree produced by MySqlParser#fullId.
    def exitFullId(self, ctx:MySqlParser.FullIdContext):
        pass


    # Enter a parse tree produced by MySqlParser#fullColumnName.
    def enterFullColumnName(self, ctx:MySqlParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by MySqlParser#fullColumnName.
    def exitFullColumnName(self, ctx:MySqlParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by MySqlParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:MySqlParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by MySqlParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:MySqlParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by MySqlParser#nullNotnull.
    def enterNullNotnull(self, ctx:MySqlParser.NullNotnullContext):
        pass

    # Exit a parse tree produced by MySqlParser#nullNotnull.
    def exitNullNotnull(self, ctx:MySqlParser.NullNotnullContext):
        pass


    # Enter a parse tree produced by MySqlParser#constant.
    def enterConstant(self, ctx:MySqlParser.ConstantContext):
        pass

    # Exit a parse tree produced by MySqlParser#constant.
    def exitConstant(self, ctx:MySqlParser.ConstantContext):
        pass


    # Enter a parse tree produced by MySqlParser#uidList.
    def enterUidList(self, ctx:MySqlParser.UidListContext):
        pass

    # Exit a parse tree produced by MySqlParser#uidList.
    def exitUidList(self, ctx:MySqlParser.UidListContext):
        pass


    # Enter a parse tree produced by MySqlParser#expressions.
    def enterExpressions(self, ctx:MySqlParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by MySqlParser#expressions.
    def exitExpressions(self, ctx:MySqlParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by MySqlParser#specificFunctionCall.
    def enterSpecificFunctionCall(self, ctx:MySqlParser.SpecificFunctionCallContext):
        pass

    # Exit a parse tree produced by MySqlParser#specificFunctionCall.
    def exitSpecificFunctionCall(self, ctx:MySqlParser.SpecificFunctionCallContext):
        pass


    # Enter a parse tree produced by MySqlParser#scalarFunctionCall.
    def enterScalarFunctionCall(self, ctx:MySqlParser.ScalarFunctionCallContext):
        pass

    # Exit a parse tree produced by MySqlParser#scalarFunctionCall.
    def exitScalarFunctionCall(self, ctx:MySqlParser.ScalarFunctionCallContext):
        pass


    # Enter a parse tree produced by MySqlParser#caseFunctionCall.
    def enterCaseFunctionCall(self, ctx:MySqlParser.CaseFunctionCallContext):
        pass

    # Exit a parse tree produced by MySqlParser#caseFunctionCall.
    def exitCaseFunctionCall(self, ctx:MySqlParser.CaseFunctionCallContext):
        pass


    # Enter a parse tree produced by MySqlParser#caseFuncAlternative.
    def enterCaseFuncAlternative(self, ctx:MySqlParser.CaseFuncAlternativeContext):
        pass

    # Exit a parse tree produced by MySqlParser#caseFuncAlternative.
    def exitCaseFuncAlternative(self, ctx:MySqlParser.CaseFuncAlternativeContext):
        pass


    # Enter a parse tree produced by MySqlParser#functionArgs.
    def enterFunctionArgs(self, ctx:MySqlParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by MySqlParser#functionArgs.
    def exitFunctionArgs(self, ctx:MySqlParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by MySqlParser#functionArg.
    def enterFunctionArg(self, ctx:MySqlParser.FunctionArgContext):
        pass

    # Exit a parse tree produced by MySqlParser#functionArg.
    def exitFunctionArg(self, ctx:MySqlParser.FunctionArgContext):
        pass


    # Enter a parse tree produced by MySqlParser#isExpression.
    def enterIsExpression(self, ctx:MySqlParser.IsExpressionContext):
        pass

    # Exit a parse tree produced by MySqlParser#isExpression.
    def exitIsExpression(self, ctx:MySqlParser.IsExpressionContext):
        pass


    # Enter a parse tree produced by MySqlParser#notExpression.
    def enterNotExpression(self, ctx:MySqlParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by MySqlParser#notExpression.
    def exitNotExpression(self, ctx:MySqlParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by MySqlParser#logicalExpression.
    def enterLogicalExpression(self, ctx:MySqlParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by MySqlParser#logicalExpression.
    def exitLogicalExpression(self, ctx:MySqlParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by MySqlParser#predicateExpression.
    def enterPredicateExpression(self, ctx:MySqlParser.PredicateExpressionContext):
        pass

    # Exit a parse tree produced by MySqlParser#predicateExpression.
    def exitPredicateExpression(self, ctx:MySqlParser.PredicateExpressionContext):
        pass


    # Enter a parse tree produced by MySqlParser#expressionAtomPredicate.
    def enterExpressionAtomPredicate(self, ctx:MySqlParser.ExpressionAtomPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#expressionAtomPredicate.
    def exitExpressionAtomPredicate(self, ctx:MySqlParser.ExpressionAtomPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#inPredicate.
    def enterInPredicate(self, ctx:MySqlParser.InPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#inPredicate.
    def exitInPredicate(self, ctx:MySqlParser.InPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#subqueryComparasionPredicate.
    def enterSubqueryComparasionPredicate(self, ctx:MySqlParser.SubqueryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#subqueryComparasionPredicate.
    def exitSubqueryComparasionPredicate(self, ctx:MySqlParser.SubqueryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx:MySqlParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx:MySqlParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#binaryComparasionPredicate.
    def enterBinaryComparasionPredicate(self, ctx:MySqlParser.BinaryComparasionPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#binaryComparasionPredicate.
    def exitBinaryComparasionPredicate(self, ctx:MySqlParser.BinaryComparasionPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#isNullPredicate.
    def enterIsNullPredicate(self, ctx:MySqlParser.IsNullPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#isNullPredicate.
    def exitIsNullPredicate(self, ctx:MySqlParser.IsNullPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#likePredicate.
    def enterLikePredicate(self, ctx:MySqlParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#likePredicate.
    def exitLikePredicate(self, ctx:MySqlParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#regexpPredicate.
    def enterRegexpPredicate(self, ctx:MySqlParser.RegexpPredicateContext):
        pass

    # Exit a parse tree produced by MySqlParser#regexpPredicate.
    def exitRegexpPredicate(self, ctx:MySqlParser.RegexpPredicateContext):
        pass


    # Enter a parse tree produced by MySqlParser#unaryExpressionAtom.
    def enterUnaryExpressionAtom(self, ctx:MySqlParser.UnaryExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#unaryExpressionAtom.
    def exitUnaryExpressionAtom(self, ctx:MySqlParser.UnaryExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#subqueryExpressionAtom.
    def enterSubqueryExpressionAtom(self, ctx:MySqlParser.SubqueryExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#subqueryExpressionAtom.
    def exitSubqueryExpressionAtom(self, ctx:MySqlParser.SubqueryExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#constantExpressionAtom.
    def enterConstantExpressionAtom(self, ctx:MySqlParser.ConstantExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#constantExpressionAtom.
    def exitConstantExpressionAtom(self, ctx:MySqlParser.ConstantExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#functionCallExpressionAtom.
    def enterFunctionCallExpressionAtom(self, ctx:MySqlParser.FunctionCallExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#functionCallExpressionAtom.
    def exitFunctionCallExpressionAtom(self, ctx:MySqlParser.FunctionCallExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#fullColumnNameExpressionAtom.
    def enterFullColumnNameExpressionAtom(self, ctx:MySqlParser.FullColumnNameExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#fullColumnNameExpressionAtom.
    def exitFullColumnNameExpressionAtom(self, ctx:MySqlParser.FullColumnNameExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#nestedExpressionAtom.
    def enterNestedExpressionAtom(self, ctx:MySqlParser.NestedExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#nestedExpressionAtom.
    def exitNestedExpressionAtom(self, ctx:MySqlParser.NestedExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#mathExpressionAtom.
    def enterMathExpressionAtom(self, ctx:MySqlParser.MathExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#mathExpressionAtom.
    def exitMathExpressionAtom(self, ctx:MySqlParser.MathExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#existsExpressionAtom.
    def enterExistsExpressionAtom(self, ctx:MySqlParser.ExistsExpressionAtomContext):
        pass

    # Exit a parse tree produced by MySqlParser#existsExpressionAtom.
    def exitExistsExpressionAtom(self, ctx:MySqlParser.ExistsExpressionAtomContext):
        pass


    # Enter a parse tree produced by MySqlParser#unaryOperator.
    def enterUnaryOperator(self, ctx:MySqlParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by MySqlParser#unaryOperator.
    def exitUnaryOperator(self, ctx:MySqlParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by MySqlParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:MySqlParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by MySqlParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:MySqlParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by MySqlParser#logicalOperator.
    def enterLogicalOperator(self, ctx:MySqlParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by MySqlParser#logicalOperator.
    def exitLogicalOperator(self, ctx:MySqlParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by MySqlParser#mathOperator.
    def enterMathOperator(self, ctx:MySqlParser.MathOperatorContext):
        pass

    # Exit a parse tree produced by MySqlParser#mathOperator.
    def exitMathOperator(self, ctx:MySqlParser.MathOperatorContext):
        pass


