lexer grammar MySqlLexer;

channels { MYSQLCOMMENT, ERRORCHANNEL }

// SKIP

SPACE:                               [ \t\r\n]+    -> channel(HIDDEN);
SPEC_MYSQL_COMMENT:                  '/*!' .+? '*/' -> channel(MYSQLCOMMENT);
COMMENT_INPUT:                       '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT:                        (
                                       ('-- ' | '#') ~[\r\n]* ('\r'? '\n' | EOF)
                                       | '--' ('\r'? '\n' | EOF)
                                     ) -> channel(HIDDEN);

ALL:                                 'ALL';
AND:                                 'AND';
AS:                                  'AS';
ASC:                                 'ASC';
BETWEEN:                             'BETWEEN';
WITH:                                'WITH';
BY:                                  'BY';
CASE:                                'CASE';
CROSS:                               'CROSS';
DESC:                                'DESC';
DISTINCT:                            'DISTINCT';
ELSE:                                'ELSE';
EXISTS:                              'EXISTS';
FALSE:                               'FALSE';
FROM:                                'FROM';
GROUP:                               'GROUP';
HAVING:                              'HAVING';
IN:                                  'IN';
INNER:                               'INNER';
INTO:                                'INTO';
IS:                                  'IS';
JOIN:                                'JOIN';
LEFT:                                'LEFT';
LIKE:                                'LIKE';
LIMIT:                               'LIMIT';
NOT:                                 'NOT';
NULL_LITERAL:                        'NULL';
ON:                                  'ON';
OR:                                  'OR';
ORDER:                               'ORDER';
OUTER:                               'OUTER';
REGEXP:                              'REGEXP';
RIGHT:                               'RIGHT';
RLIKE:                               'RLIKE';
SELECT:                              'SELECT';
THEN:                                'THEN';
TRUE:                                'TRUE';
UNION:                               'UNION';
USING:                               'USING';
VALUES:                              'VALUES';
WHEN:                                'WHEN';
WHERE:                               'WHERE';

//// Common Keywords, but can be ID
//
ANY:                                 'ANY';
END:                                 'END';
OFFSET:                              'OFFSET';
SOME:                                'SOME';
UNKNOWN:                             'UNKNOWN';

//// Operators. Arithmetics

STAR:                                '*';
DIVIDE:                              '/';
MODULE:                              '%';
PLUS:                                '+';
MINUSMINUS:                          '--';
MINUS:                               '-';
DIV:                                 'DIV';
MOD:                                 'MOD';

//// Operators. Comparation

EQUAL_SYMBOL:                        '=';
GREATER_SYMBOL:                      '>';
LESS_SYMBOL:                         '<';
EXCLAMATION_SYMBOL:                  '!';

//// Operators. Bit

BIT_NOT_OP:                          '~';
BIT_OR_OP:                           '|';
BIT_AND_OP:                          '&';
BIT_XOR_OP:                          '^';

//// Constructors symbols

DOT:                                 '.';
LR_BRACKET:                          '(';
RR_BRACKET:                          ')';
COMMA:                               ',';

//// Literal Primitives

STRING_LITERAL:                      DQUOTA_STRING | SQUOTA_STRING;
DECIMAL_LITERAL:                     DEC_DIGIT+;

REAL_LITERAL:                        (DEC_DIGIT+)? '.' DEC_DIGIT+;
NULL_SPEC_LITERAL:                   '\\' 'N';

DOT_ID:                              '.' ID_LITERAL;

//// Identifiers

ID:                                  ID_LITERAL;

fragment ID_LITERAL:                 [A-Za-z_$0-9]*?[A-Za-z_$]+?[A-Za-z_$0-9]*;
fragment DQUOTA_STRING:              '"' ( '\\'. | '""' | ~('"'| '\\') )* '"';
fragment SQUOTA_STRING:              '\'' ('\\'. | '\'\'' | ~('\'' | '\\'))* '\'';
fragment BQUOTA_STRING:              '`' ( '\\'. | '``' | ~('`'|'\\'))* '`';
fragment DEC_DIGIT:                  [0-9];

// Last tokens must generate Errors

ERROR_RECONGNIGION:                  .    -> channel(ERRORCHANNEL);
