parser grammar MySqlParser;

options { tokenVocab=MySqlLexer; }

// 1
selectStatement
    : querySpecification                                            #simpleSelect
    | queryExpression                                               #parenthesisSelect
    ;

// 2
orderByClause
    : ORDER BY orderByExpression (',' orderByExpression)*
    ;

// 3
orderByExpression
    : expression order=(ASC | DESC)?
    ;

// 4
tableSource
    : tableSourceItem joinPart*                                     #tableSourceBase
    | '(' tableSourceItem joinPart* ')'                             #tableSourceNested
    ;

// 5
tableSources
    : tableSource (',' tableSource)*
    ;

// 6
tableSourceItem
    : fullId (AS? alias=ID)?                                        #atomTableItem
    | (
      selectStatement
      | '(' parenthesisSubquery=selectStatement ')'
      )
      AS? alias=ID                                                  #subqueryTableItem
    | '(' tableSources ')'                                          #tableSourcesItem
    ;

// 7
joinPart
    : (INNER | CROSS)? JOIN tableSourceItem                         #innerJoin
    | (LEFT | RIGHT) OUTER? JOIN tableSourceItem
        (
          ON expression
          | USING '(' uidList ')'
        )                                                           #outerJoin
    ;

// 8
queryExpression
    : '(' querySpecification ')'
    | '(' queryExpression ')'
    ;

// 9
querySpecification
    : SELECT DISTINCT? selectElements
      fromClause? orderByClause? limitClause?
    ;

// 12
selectElements
    : (star='*' | selectElement ) (',' selectElement)*
    ;

// 13
selectElement
    : fullColumnName (AS? ID)?                                      #selectColumnElement
    | functionCall (AS? ID)?                                        #selectFunctionElement
    | expression (AS? ID)?                                          #selectExpressionElement
    ;

// 14
fromClause
    : FROM tableSources
      (WHERE whereExpr=expression)?
      (
        GROUP BY
        groupByItem (',' groupByItem)*
        (HAVING havingExpr=expression)?
      )?
    ;

// 15
groupByItem
    : expression order=(ASC | DESC)?
    ;

// 16
limitClause
    : LIMIT
    (
      (offset=DECIMAL_LITERAL ',')? limit=DECIMAL_LITERAL
      | limit=DECIMAL_LITERAL OFFSET offset=DECIMAL_LITERAL
    )
    ;

// 17
fullId
    : ID DOT_ID?
    ;

// 18
fullColumnName
    : ID (DOT_ID DOT_ID? )?
    ;

// 19
booleanLiteral
    : TRUE | FALSE;

// 20
nullNotnull
    : NOT? (NULL_LITERAL | NULL_SPEC_LITERAL)
    ;

// 21
constant
    : STRING_LITERAL | DECIMAL_LITERAL
    | '-' DECIMAL_LITERAL
    | booleanLiteral
    | REAL_LITERAL
    | NOT? nullLiteral=(NULL_LITERAL | NULL_SPEC_LITERAL)
    ;

// 22
uidList
    : ID (',' ID)*
    ;

// 23
expressions
    : expression (',' expression)*
    ;

// 24
functionCall
    : specificFunction                                              #specificFunctionCall
//    | aggregateWindowedFunction                                     #aggregateFunctionCall
    | ID '(' functionArgs? ')'                                      #scalarFunctionCall
    ;

// 25
specificFunction
    :CASE caseFuncAlternative+
      (ELSE elseArg=functionArg)? END                               #caseFunctionCall
    ;

// 26
caseFuncAlternative
    : WHEN condition=functionArg
      THEN consequent=functionArg
    ;

//// 27
//aggregateWindowedFunction
//    : (AVG | MAX | MIN | SUM)
//      '(' aggregator=(ALL | DISTINCT)? functionArg ')'
//    | COUNT '(' (starArg='*' | aggregator=ALL? functionArg) ')'
//    | COUNT '(' aggregator=DISTINCT functionArgs ')'
//    ;

// 28
functionArgs
    : ('*' | ALL | constant | fullColumnName | functionCall | expression)
    (
      ','
      ('*' | ALL | constant | fullColumnName | functionCall | expression)
    )*
    ;

// 29
functionArg
    : constant | fullColumnName | functionCall | expression
    ;

// 30
expression
    : notOperator=(NOT | '!') expression                            #notExpression
    | expression logicalOperator expression                         #logicalExpression
    | predicate IS NOT? testValue=(TRUE | FALSE | UNKNOWN)          #isExpression
    | predicate                                                     #predicateExpression
    ;

// 31
predicate
    : predicate NOT? IN '(' (selectStatement | expressions) ')'     #inPredicate
    | predicate IS nullNotnull                                      #isNullPredicate
    | left=predicate comparisonOperator right=predicate             #binaryComparasionPredicate
    | predicate comparisonOperator
      quantifier=(ALL | ANY | SOME) '(' selectStatement ')'         #subqueryComparasionPredicate
    | predicate NOT? BETWEEN predicate AND predicate                #betweenPredicate
    | predicate NOT? LIKE predicate                                 #likePredicate
    | predicate NOT? regex=(REGEXP | RLIKE) predicate               #regexpPredicate
    | expressionAtom                                                #expressionAtomPredicate
    ;

// 32
expressionAtom
    : constant                                                      #constantExpressionAtom
    | fullColumnName                                                #fullColumnNameExpressionAtom
    | functionCall                                                  #functionCallExpressionAtom
    | unaryOperator expressionAtom                                  #unaryExpressionAtom
    | '(' expression (',' expression)* ')'                          #nestedExpressionAtom
    | EXISTS '(' selectStatement ')'                                #existsExpressionAtom
    | '(' selectStatement ')'                                       #subqueryExpressionAtom
    | left=expressionAtom mathOperator right=expressionAtom         #mathExpressionAtom
    ;

// 33
unaryOperator
    : '!' | '~' | '+' | '-' | NOT
    ;

// 34
comparisonOperator
    : '=' | '>' | '<' | '<' '=' | '>' '='
    | '<' '>' | '!' '=' | '<' '=' '>'
    ;

// 35
logicalOperator
    : AND | OR
    ;

// 36
mathOperator
    : '*' | '/' | '%' | DIV | MOD | '+' | '-' | '--'
    ;
