# Generated from /Users/zhangzhiqiang/PycharmProjects/PyLinq/PyLinq/parser/MySqlParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3O")
        buf.write("\u01f0\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\5\2G\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3N\n\3\f\3\16\3Q\13\3\3\4\3\4\5\4U\n")
        buf.write("\4\3\5\3\5\7\5Y\n\5\f\5\16\5\\\13\5\3\5\3\5\3\5\7\5a\n")
        buf.write("\5\f\5\16\5d\13\5\3\5\3\5\5\5h\n\5\3\6\3\6\3\6\7\6m\n")
        buf.write("\6\f\6\16\6p\13\6\3\7\3\7\5\7t\n\7\3\7\5\7w\n\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7~\n\7\3\7\5\7\u0081\n\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u0089\n\7\3\b\5\b\u008c\n\b\3\b\3\b\3")
        buf.write("\b\3\b\5\b\u0092\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\5\b\u009d\n\b\5\b\u009f\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u00a9\n\t\3\n\3\n\5\n\u00ad\n\n\3\n\3\n\5")
        buf.write("\n\u00b1\n\n\3\n\5\n\u00b4\n\n\3\n\5\n\u00b7\n\n\3\13")
        buf.write("\3\13\5\13\u00bb\n\13\3\13\3\13\7\13\u00bf\n\13\f\13\16")
        buf.write("\13\u00c2\13\13\3\f\3\f\5\f\u00c6\n\f\3\f\5\f\u00c9\n")
        buf.write("\f\3\f\3\f\5\f\u00cd\n\f\3\f\5\f\u00d0\n\f\3\f\3\f\5\f")
        buf.write("\u00d4\n\f\3\f\5\f\u00d7\n\f\5\f\u00d9\n\f\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00df\n\r\3\r\3\r\3\r\3\r\3\r\7\r\u00e6\n\r\f")
        buf.write("\r\16\r\u00e9\13\r\3\r\3\r\5\r\u00ed\n\r\5\r\u00ef\n\r")
        buf.write("\3\16\3\16\5\16\u00f3\n\16\3\17\3\17\3\17\5\17\u00f8\n")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00fe\n\17\3\20\3\20\5\20")
        buf.write("\u0102\n\20\3\21\3\21\3\21\5\21\u0107\n\21\5\21\u0109")
        buf.write("\n\21\3\22\3\22\3\23\5\23\u010e\n\23\3\23\3\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\5\24\u0119\n\24\3\24\5\24")
        buf.write("\u011c\n\24\3\25\3\25\3\25\7\25\u0121\n\25\f\25\16\25")
        buf.write("\u0124\13\25\3\26\3\26\3\26\7\26\u0129\n\26\f\26\16\26")
        buf.write("\u012c\13\26\3\27\3\27\3\27\3\27\5\27\u0132\n\27\3\27")
        buf.write("\5\27\u0135\n\27\3\30\3\30\6\30\u0139\n\30\r\30\16\30")
        buf.write("\u013a\3\30\3\30\5\30\u013f\n\30\3\30\3\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u014e")
        buf.write("\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0157\n")
        buf.write("\32\7\32\u0159\n\32\f\32\16\32\u015c\13\32\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0162\n\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u016a\n\34\3\34\3\34\3\34\5\34\u016f\n\34\3\34\3")
        buf.write("\34\3\34\3\34\7\34\u0175\n\34\f\34\16\34\u0178\13\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0183")
        buf.write("\n\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u018c\n")
        buf.write("\35\3\35\3\35\3\35\3\35\5\35\u0192\n\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u0198\n\35\3\35\3\35\3\35\3\35\5\35\u019e\n")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\7\35\u01ac\n\35\f\35\16\35\u01af\13\35\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36")
        buf.write("\u01bc\n\36\f\36\16\36\u01bf\13\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u01cc\n\36\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\7\36\u01d5\n\36\f\36")
        buf.write("\16\36\u01d8\13\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \5 \u01ea\n \3!\3!\3\"\3\"\3\"\2\5\66")
        buf.write("8:#\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@B\2\17\4\2\n\n\17\17\4\2\16\16\30\30\4\2")
        buf.write("\34\34&&\4\2\23\23**\4\2  LL\4\2\37\37@@\5\2\23\23**\64")
        buf.write("\64\4\2%%\'\'\5\2\7\7\60\60\63\63\4\2\65\67;<\6\2\37\37")
        buf.write("88::@A\4\2\b\b\"\"\3\28:\2\u0233\2F\3\2\2\2\4H\3\2\2\2")
        buf.write("\6R\3\2\2\2\bg\3\2\2\2\ni\3\2\2\2\f\u0088\3\2\2\2\16\u009e")
        buf.write("\3\2\2\2\20\u00a8\3\2\2\2\22\u00aa\3\2\2\2\24\u00ba\3")
        buf.write("\2\2\2\26\u00d8\3\2\2\2\30\u00da\3\2\2\2\32\u00f0\3\2")
        buf.write("\2\2\34\u00f4\3\2\2\2\36\u00ff\3\2\2\2 \u0103\3\2\2\2")
        buf.write("\"\u010a\3\2\2\2$\u010d\3\2\2\2&\u011b\3\2\2\2(\u011d")
        buf.write("\3\2\2\2*\u0125\3\2\2\2,\u0134\3\2\2\2.\u0136\3\2\2\2")
        buf.write("\60\u0142\3\2\2\2\62\u014d\3\2\2\2\64\u0161\3\2\2\2\66")
        buf.write("\u016e\3\2\2\28\u0179\3\2\2\2:\u01cb\3\2\2\2<\u01d9\3")
        buf.write("\2\2\2>\u01e9\3\2\2\2@\u01eb\3\2\2\2B\u01ed\3\2\2\2DG")
        buf.write("\5\22\n\2EG\5\20\t\2FD\3\2\2\2FE\3\2\2\2G\3\3\2\2\2HI")
        buf.write("\7#\2\2IJ\7\f\2\2JO\5\6\4\2KL\7H\2\2LN\5\6\4\2MK\3\2\2")
        buf.write("\2NQ\3\2\2\2OM\3\2\2\2OP\3\2\2\2P\5\3\2\2\2QO\3\2\2\2")
        buf.write("RT\5\66\34\2SU\t\2\2\2TS\3\2\2\2TU\3\2\2\2U\7\3\2\2\2")
        buf.write("VZ\5\f\7\2WY\5\16\b\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z")
        buf.write("[\3\2\2\2[h\3\2\2\2\\Z\3\2\2\2]^\7F\2\2^b\5\f\7\2_a\5")
        buf.write("\16\b\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2ce\3\2")
        buf.write("\2\2db\3\2\2\2ef\7G\2\2fh\3\2\2\2gV\3\2\2\2g]\3\2\2\2")
        buf.write("h\t\3\2\2\2in\5\b\5\2jk\7H\2\2km\5\b\5\2lj\3\2\2\2mp\3")
        buf.write("\2\2\2nl\3\2\2\2no\3\2\2\2o\13\3\2\2\2pn\3\2\2\2qv\5\36")
        buf.write("\20\2rt\7\t\2\2sr\3\2\2\2st\3\2\2\2tu\3\2\2\2uw\7N\2\2")
        buf.write("vs\3\2\2\2vw\3\2\2\2w\u0089\3\2\2\2x~\5\2\2\2yz\7F\2\2")
        buf.write("z{\5\2\2\2{|\7G\2\2|~\3\2\2\2}x\3\2\2\2}y\3\2\2\2~\u0080")
        buf.write("\3\2\2\2\177\u0081\7\t\2\2\u0080\177\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083\7N\2\2\u0083")
        buf.write("\u0089\3\2\2\2\u0084\u0085\7F\2\2\u0085\u0086\5\n\6\2")
        buf.write("\u0086\u0087\7G\2\2\u0087\u0089\3\2\2\2\u0088q\3\2\2\2")
        buf.write("\u0088}\3\2\2\2\u0088\u0084\3\2\2\2\u0089\r\3\2\2\2\u008a")
        buf.write("\u008c\t\3\2\2\u008b\u008a\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\7\33\2\2\u008e\u009f")
        buf.write("\5\f\7\2\u008f\u0091\t\4\2\2\u0090\u0092\7$\2\2\u0091")
        buf.write("\u0090\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0093\3\2\2\2")
        buf.write("\u0093\u0094\7\33\2\2\u0094\u009c\5\f\7\2\u0095\u0096")
        buf.write("\7!\2\2\u0096\u009d\5\66\34\2\u0097\u0098\7,\2\2\u0098")
        buf.write("\u0099\7F\2\2\u0099\u009a\5(\25\2\u009a\u009b\7G\2\2\u009b")
        buf.write("\u009d\3\2\2\2\u009c\u0095\3\2\2\2\u009c\u0097\3\2\2\2")
        buf.write("\u009d\u009f\3\2\2\2\u009e\u008b\3\2\2\2\u009e\u008f\3")
        buf.write("\2\2\2\u009f\17\3\2\2\2\u00a0\u00a1\7F\2\2\u00a1\u00a2")
        buf.write("\5\22\n\2\u00a2\u00a3\7G\2\2\u00a3\u00a9\3\2\2\2\u00a4")
        buf.write("\u00a5\7F\2\2\u00a5\u00a6\5\20\t\2\u00a6\u00a7\7G\2\2")
        buf.write("\u00a7\u00a9\3\2\2\2\u00a8\u00a0\3\2\2\2\u00a8\u00a4\3")
        buf.write("\2\2\2\u00a9\21\3\2\2\2\u00aa\u00ac\7(\2\2\u00ab\u00ad")
        buf.write("\7\20\2\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00ae\3\2\2\2\u00ae\u00b0\5\24\13\2\u00af\u00b1\5\30")
        buf.write("\r\2\u00b0\u00af\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b3")
        buf.write("\3\2\2\2\u00b2\u00b4\5\4\3\2\u00b3\u00b2\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b7\5\34\17")
        buf.write("\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\23\3")
        buf.write("\2\2\2\u00b8\u00bb\7\65\2\2\u00b9\u00bb\5\26\f\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00b9\3\2\2\2\u00bb\u00c0\3\2\2\2")
        buf.write("\u00bc\u00bd\7H\2\2\u00bd\u00bf\5\26\f\2\u00be\u00bc\3")
        buf.write("\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\25\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c8")
        buf.write("\5 \21\2\u00c4\u00c6\7\t\2\2\u00c5\u00c4\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\7N\2\2")
        buf.write("\u00c8\u00c5\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00d9\3")
        buf.write("\2\2\2\u00ca\u00cf\5,\27\2\u00cb\u00cd\7\t\2\2\u00cc\u00cb")
        buf.write("\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00d0\7N\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00d0\u00d9\3\2\2\2\u00d1\u00d6\5\66\34\2\u00d2\u00d4")
        buf.write("\7\t\2\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d7\7N\2\2\u00d6\u00d3\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00c3\3")
        buf.write("\2\2\2\u00d8\u00ca\3\2\2\2\u00d8\u00d1\3\2\2\2\u00d9\27")
        buf.write("\3\2\2\2\u00da\u00db\7\24\2\2\u00db\u00de\5\n\6\2\u00dc")
        buf.write("\u00dd\7/\2\2\u00dd\u00df\5\66\34\2\u00de\u00dc\3\2\2")
        buf.write("\2\u00de\u00df\3\2\2\2\u00df\u00ee\3\2\2\2\u00e0\u00e1")
        buf.write("\7\25\2\2\u00e1\u00e2\7\f\2\2\u00e2\u00e7\5\32\16\2\u00e3")
        buf.write("\u00e4\7H\2\2\u00e4\u00e6\5\32\16\2\u00e5\u00e3\3\2\2")
        buf.write("\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8")
        buf.write("\3\2\2\2\u00e8\u00ec\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea")
        buf.write("\u00eb\7\26\2\2\u00eb\u00ed\5\66\34\2\u00ec\u00ea\3\2")
        buf.write("\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00e0")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\31\3\2\2\2\u00f0\u00f2")
        buf.write("\5\66\34\2\u00f1\u00f3\t\2\2\2\u00f2\u00f1\3\2\2\2\u00f2")
        buf.write("\u00f3\3\2\2\2\u00f3\33\3\2\2\2\u00f4\u00fd\7\36\2\2\u00f5")
        buf.write("\u00f6\7J\2\2\u00f6\u00f8\7H\2\2\u00f7\u00f5\3\2\2\2\u00f7")
        buf.write("\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fe\7J\2\2")
        buf.write("\u00fa\u00fb\7J\2\2\u00fb\u00fc\7\62\2\2\u00fc\u00fe\7")
        buf.write("J\2\2\u00fd\u00f7\3\2\2\2\u00fd\u00fa\3\2\2\2\u00fe\35")
        buf.write("\3\2\2\2\u00ff\u0101\7N\2\2\u0100\u0102\7M\2\2\u0101\u0100")
        buf.write("\3\2\2\2\u0101\u0102\3\2\2\2\u0102\37\3\2\2\2\u0103\u0108")
        buf.write("\7N\2\2\u0104\u0106\7M\2\2\u0105\u0107\7M\2\2\u0106\u0105")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108")
        buf.write("\u0104\3\2\2\2\u0108\u0109\3\2\2\2\u0109!\3\2\2\2\u010a")
        buf.write("\u010b\t\5\2\2\u010b#\3\2\2\2\u010c\u010e\7\37\2\2\u010d")
        buf.write("\u010c\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0110\t\6\2\2\u0110%\3\2\2\2\u0111\u011c\7I\2\2")
        buf.write("\u0112\u011c\7J\2\2\u0113\u0114\7:\2\2\u0114\u011c\7J")
        buf.write("\2\2\u0115\u011c\5\"\22\2\u0116\u011c\7K\2\2\u0117\u0119")
        buf.write("\7\37\2\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119")
        buf.write("\u011a\3\2\2\2\u011a\u011c\t\6\2\2\u011b\u0111\3\2\2\2")
        buf.write("\u011b\u0112\3\2\2\2\u011b\u0113\3\2\2\2\u011b\u0115\3")
        buf.write("\2\2\2\u011b\u0116\3\2\2\2\u011b\u0118\3\2\2\2\u011c\'")
        buf.write("\3\2\2\2\u011d\u0122\7N\2\2\u011e\u011f\7H\2\2\u011f\u0121")
        buf.write("\7N\2\2\u0120\u011e\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123)\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0125\u012a\5\66\34\2\u0126\u0127\7H\2")
        buf.write("\2\u0127\u0129\5\66\34\2\u0128\u0126\3\2\2\2\u0129\u012c")
        buf.write("\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b")
        buf.write("+\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u0135\5.\30\2\u012e")
        buf.write("\u012f\7N\2\2\u012f\u0131\7F\2\2\u0130\u0132\5\62\32\2")
        buf.write("\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133\3")
        buf.write("\2\2\2\u0133\u0135\7G\2\2\u0134\u012d\3\2\2\2\u0134\u012e")
        buf.write("\3\2\2\2\u0135-\3\2\2\2\u0136\u0138\7\r\2\2\u0137\u0139")
        buf.write("\5\60\31\2\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2\u013a")
        buf.write("\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013e\3\2\2\2")
        buf.write("\u013c\u013d\7\21\2\2\u013d\u013f\5\64\33\2\u013e\u013c")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\3\2\2\2\u0140")
        buf.write("\u0141\7\61\2\2\u0141/\3\2\2\2\u0142\u0143\7.\2\2\u0143")
        buf.write("\u0144\5\64\33\2\u0144\u0145\7)\2\2\u0145\u0146\5\64\33")
        buf.write("\2\u0146\61\3\2\2\2\u0147\u014e\7\65\2\2\u0148\u014e\7")
        buf.write("\7\2\2\u0149\u014e\5&\24\2\u014a\u014e\5 \21\2\u014b\u014e")
        buf.write("\5,\27\2\u014c\u014e\5\66\34\2\u014d\u0147\3\2\2\2\u014d")
        buf.write("\u0148\3\2\2\2\u014d\u0149\3\2\2\2\u014d\u014a\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014e\u015a\3")
        buf.write("\2\2\2\u014f\u0156\7H\2\2\u0150\u0157\7\65\2\2\u0151\u0157")
        buf.write("\7\7\2\2\u0152\u0157\5&\24\2\u0153\u0157\5 \21\2\u0154")
        buf.write("\u0157\5,\27\2\u0155\u0157\5\66\34\2\u0156\u0150\3\2\2")
        buf.write("\2\u0156\u0151\3\2\2\2\u0156\u0152\3\2\2\2\u0156\u0153")
        buf.write("\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157")
        buf.write("\u0159\3\2\2\2\u0158\u014f\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\63\3\2")
        buf.write("\2\2\u015c\u015a\3\2\2\2\u015d\u0162\5&\24\2\u015e\u0162")
        buf.write("\5 \21\2\u015f\u0162\5,\27\2\u0160\u0162\5\66\34\2\u0161")
        buf.write("\u015d\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u015f\3\2\2\2")
        buf.write("\u0161\u0160\3\2\2\2\u0162\65\3\2\2\2\u0163\u0164\b\34")
        buf.write("\1\2\u0164\u0165\t\7\2\2\u0165\u016f\5\66\34\6\u0166\u0167")
        buf.write("\58\35\2\u0167\u0169\7\32\2\2\u0168\u016a\7\37\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016c\t\b\2\2\u016c\u016f\3\2\2\2\u016d\u016f\5")
        buf.write("8\35\2\u016e\u0163\3\2\2\2\u016e\u0166\3\2\2\2\u016e\u016d")
        buf.write("\3\2\2\2\u016f\u0176\3\2\2\2\u0170\u0171\f\5\2\2\u0171")
        buf.write("\u0172\5@!\2\u0172\u0173\5\66\34\6\u0173\u0175\3\2\2\2")
        buf.write("\u0174\u0170\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3")
        buf.write("\2\2\2\u0176\u0177\3\2\2\2\u0177\67\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0179\u017a\b\35\1\2\u017a\u017b\5:\36\2\u017b")
        buf.write("\u01ad\3\2\2\2\u017c\u017d\f\b\2\2\u017d\u017e\5> \2\u017e")
        buf.write("\u017f\58\35\t\u017f\u01ac\3\2\2\2\u0180\u0182\f\6\2\2")
        buf.write("\u0181\u0183\7\37\2\2\u0182\u0181\3\2\2\2\u0182\u0183")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0185\7\13\2\2\u0185")
        buf.write("\u0186\58\35\2\u0186\u0187\7\b\2\2\u0187\u0188\58\35\7")
        buf.write("\u0188\u01ac\3\2\2\2\u0189\u018b\f\5\2\2\u018a\u018c\7")
        buf.write("\37\2\2\u018b\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018e\7\35\2\2\u018e\u01ac\58\35")
        buf.write("\6\u018f\u0191\f\4\2\2\u0190\u0192\7\37\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0194\t\t\2\2\u0194\u01ac\58\35\5\u0195\u0197\f\n\2\2")
        buf.write("\u0196\u0198\7\37\2\2\u0197\u0196\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\7\27\2\2\u019a")
        buf.write("\u019d\7F\2\2\u019b\u019e\5\2\2\2\u019c\u019e\5*\26\2")
        buf.write("\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e\u019f\3")
        buf.write("\2\2\2\u019f\u01a0\7G\2\2\u01a0\u01ac\3\2\2\2\u01a1\u01a2")
        buf.write("\f\t\2\2\u01a2\u01a3\7\32\2\2\u01a3\u01ac\5$\23\2\u01a4")
        buf.write("\u01a5\f\7\2\2\u01a5\u01a6\5> \2\u01a6\u01a7\t\n\2\2\u01a7")
        buf.write("\u01a8\7F\2\2\u01a8\u01a9\5\2\2\2\u01a9\u01aa\7G\2\2\u01aa")
        buf.write("\u01ac\3\2\2\2\u01ab\u017c\3\2\2\2\u01ab\u0180\3\2\2\2")
        buf.write("\u01ab\u0189\3\2\2\2\u01ab\u018f\3\2\2\2\u01ab\u0195\3")
        buf.write("\2\2\2\u01ab\u01a1\3\2\2\2\u01ab\u01a4\3\2\2\2\u01ac\u01af")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("9\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\b\36\1\2\u01b1")
        buf.write("\u01cc\5&\24\2\u01b2\u01cc\5 \21\2\u01b3\u01cc\5,\27\2")
        buf.write("\u01b4\u01b5\5<\37\2\u01b5\u01b6\5:\36\b\u01b6\u01cc\3")
        buf.write("\2\2\2\u01b7\u01b8\7F\2\2\u01b8\u01bd\5\66\34\2\u01b9")
        buf.write("\u01ba\7H\2\2\u01ba\u01bc\5\66\34\2\u01bb\u01b9\3\2\2")
        buf.write("\2\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01be")
        buf.write("\3\2\2\2\u01be\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2\u01c0")
        buf.write("\u01c1\7G\2\2\u01c1\u01cc\3\2\2\2\u01c2\u01c3\7\22\2\2")
        buf.write("\u01c3\u01c4\7F\2\2\u01c4\u01c5\5\2\2\2\u01c5\u01c6\7")
        buf.write("G\2\2\u01c6\u01cc\3\2\2\2\u01c7\u01c8\7F\2\2\u01c8\u01c9")
        buf.write("\5\2\2\2\u01c9\u01ca\7G\2\2\u01ca\u01cc\3\2\2\2\u01cb")
        buf.write("\u01b0\3\2\2\2\u01cb\u01b2\3\2\2\2\u01cb\u01b3\3\2\2\2")
        buf.write("\u01cb\u01b4\3\2\2\2\u01cb\u01b7\3\2\2\2\u01cb\u01c2\3")
        buf.write("\2\2\2\u01cb\u01c7\3\2\2\2\u01cc\u01d6\3\2\2\2\u01cd\u01ce")
        buf.write("\f\4\2\2\u01ce\u01cf\t\13\2\2\u01cf\u01d5\5:\36\5\u01d0")
        buf.write("\u01d1\f\3\2\2\u01d1\u01d2\5B\"\2\u01d2\u01d3\5:\36\4")
        buf.write("\u01d3\u01d5\3\2\2\2\u01d4\u01cd\3\2\2\2\u01d4\u01d0\3")
        buf.write("\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7")
        buf.write("\3\2\2\2\u01d7;\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01da")
        buf.write("\t\f\2\2\u01da=\3\2\2\2\u01db\u01ea\7=\2\2\u01dc\u01ea")
        buf.write("\7>\2\2\u01dd\u01ea\7?\2\2\u01de\u01df\7?\2\2\u01df\u01ea")
        buf.write("\7=\2\2\u01e0\u01e1\7>\2\2\u01e1\u01ea\7=\2\2\u01e2\u01e3")
        buf.write("\7?\2\2\u01e3\u01ea\7>\2\2\u01e4\u01e5\7@\2\2\u01e5\u01ea")
        buf.write("\7=\2\2\u01e6\u01e7\7?\2\2\u01e7\u01e8\7=\2\2\u01e8\u01ea")
        buf.write("\7>\2\2\u01e9\u01db\3\2\2\2\u01e9\u01dc\3\2\2\2\u01e9")
        buf.write("\u01dd\3\2\2\2\u01e9\u01de\3\2\2\2\u01e9\u01e0\3\2\2\2")
        buf.write("\u01e9\u01e2\3\2\2\2\u01e9\u01e4\3\2\2\2\u01e9\u01e6\3")
        buf.write("\2\2\2\u01ea?\3\2\2\2\u01eb\u01ec\t\r\2\2\u01ecA\3\2\2")
        buf.write("\2\u01ed\u01ee\t\16\2\2\u01eeC\3\2\2\2FFOTZbgnsv}\u0080")
        buf.write("\u0088\u008b\u0091\u009c\u009e\u00a8\u00ac\u00b0\u00b3")
        buf.write("\u00b6\u00ba\u00c0\u00c5\u00c8\u00cc\u00cf\u00d3\u00d6")
        buf.write("\u00d8\u00de\u00e7\u00ec\u00ee\u00f2\u00f7\u00fd\u0101")
        buf.write("\u0106\u0108\u010d\u0118\u011b\u0122\u012a\u0131\u0134")
        buf.write("\u013a\u013e\u014d\u0156\u015a\u0161\u0169\u016e\u0176")
        buf.write("\u0182\u018b\u0191\u0197\u019d\u01ab\u01ad\u01bd\u01cb")
        buf.write("\u01d4\u01d6\u01e9")
        return buf.getvalue()


class MySqlParser ( Parser ):

    grammarFileName = "MySqlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'ALL'", "'AND'", "'AS'", "'ASC'", "'BETWEEN'", 
                     "'BY'", "'CASE'", "'CROSS'", "'DESC'", "'DISTINCT'", 
                     "'ELSE'", "'EXISTS'", "'FALSE'", "'FROM'", "'GROUP'", 
                     "'HAVING'", "'IN'", "'INNER'", "'INTO'", "'IS'", "'JOIN'", 
                     "'LEFT'", "'LIKE'", "'LIMIT'", "'NOT'", "'NULL'", "'ON'", 
                     "'OR'", "'ORDER'", "'OUTER'", "'REGEXP'", "'RIGHT'", 
                     "'RLIKE'", "'SELECT'", "'THEN'", "'TRUE'", "'UNION'", 
                     "'USING'", "'VALUES'", "'WHEN'", "'WHERE'", "'ANY'", 
                     "'END'", "'OFFSET'", "'SOME'", "'UNKNOWN'", "'*'", 
                     "'/'", "'%'", "'+'", "'--'", "'-'", "'DIV'", "'MOD'", 
                     "'='", "'>'", "'<'", "'!'", "'~'", "'|'", "'&'", "'^'", 
                     "'.'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "SPACE", "SPEC_MYSQL_COMMENT", "COMMENT_INPUT", 
                      "LINE_COMMENT", "ALL", "AND", "AS", "ASC", "BETWEEN", 
                      "BY", "CASE", "CROSS", "DESC", "DISTINCT", "ELSE", 
                      "EXISTS", "FALSE", "FROM", "GROUP", "HAVING", "IN", 
                      "INNER", "INTO", "IS", "JOIN", "LEFT", "LIKE", "LIMIT", 
                      "NOT", "NULL_LITERAL", "ON", "OR", "ORDER", "OUTER", 
                      "REGEXP", "RIGHT", "RLIKE", "SELECT", "THEN", "TRUE", 
                      "UNION", "USING", "VALUES", "WHEN", "WHERE", "ANY", 
                      "END", "OFFSET", "SOME", "UNKNOWN", "STAR", "DIVIDE", 
                      "MODULE", "PLUS", "MINUSMINUS", "MINUS", "DIV", "MOD", 
                      "EQUAL_SYMBOL", "GREATER_SYMBOL", "LESS_SYMBOL", "EXCLAMATION_SYMBOL", 
                      "BIT_NOT_OP", "BIT_OR_OP", "BIT_AND_OP", "BIT_XOR_OP", 
                      "DOT", "LR_BRACKET", "RR_BRACKET", "COMMA", "STRING_LITERAL", 
                      "DECIMAL_LITERAL", "REAL_LITERAL", "NULL_SPEC_LITERAL", 
                      "DOT_ID", "ID", "ERROR_RECONGNIGION" ]

    RULE_selectStatement = 0
    RULE_orderByClause = 1
    RULE_orderByExpression = 2
    RULE_tableSource = 3
    RULE_tableSources = 4
    RULE_tableSourceItem = 5
    RULE_joinPart = 6
    RULE_queryExpression = 7
    RULE_querySpecification = 8
    RULE_selectElements = 9
    RULE_selectElement = 10
    RULE_fromClause = 11
    RULE_groupByItem = 12
    RULE_limitClause = 13
    RULE_fullId = 14
    RULE_fullColumnName = 15
    RULE_booleanLiteral = 16
    RULE_nullNotnull = 17
    RULE_constant = 18
    RULE_uidList = 19
    RULE_expressions = 20
    RULE_functionCall = 21
    RULE_specificFunction = 22
    RULE_caseFuncAlternative = 23
    RULE_functionArgs = 24
    RULE_functionArg = 25
    RULE_expression = 26
    RULE_predicate = 27
    RULE_expressionAtom = 28
    RULE_unaryOperator = 29
    RULE_comparisonOperator = 30
    RULE_logicalOperator = 31
    RULE_mathOperator = 32

    ruleNames =  [ "selectStatement", "orderByClause", "orderByExpression", 
                   "tableSource", "tableSources", "tableSourceItem", "joinPart", 
                   "queryExpression", "querySpecification", "selectElements", 
                   "selectElement", "fromClause", "groupByItem", "limitClause", 
                   "fullId", "fullColumnName", "booleanLiteral", "nullNotnull", 
                   "constant", "uidList", "expressions", "functionCall", 
                   "specificFunction", "caseFuncAlternative", "functionArgs", 
                   "functionArg", "expression", "predicate", "expressionAtom", 
                   "unaryOperator", "comparisonOperator", "logicalOperator", 
                   "mathOperator" ]

    EOF = Token.EOF
    SPACE=1
    SPEC_MYSQL_COMMENT=2
    COMMENT_INPUT=3
    LINE_COMMENT=4
    ALL=5
    AND=6
    AS=7
    ASC=8
    BETWEEN=9
    BY=10
    CASE=11
    CROSS=12
    DESC=13
    DISTINCT=14
    ELSE=15
    EXISTS=16
    FALSE=17
    FROM=18
    GROUP=19
    HAVING=20
    IN=21
    INNER=22
    INTO=23
    IS=24
    JOIN=25
    LEFT=26
    LIKE=27
    LIMIT=28
    NOT=29
    NULL_LITERAL=30
    ON=31
    OR=32
    ORDER=33
    OUTER=34
    REGEXP=35
    RIGHT=36
    RLIKE=37
    SELECT=38
    THEN=39
    TRUE=40
    UNION=41
    USING=42
    VALUES=43
    WHEN=44
    WHERE=45
    ANY=46
    END=47
    OFFSET=48
    SOME=49
    UNKNOWN=50
    STAR=51
    DIVIDE=52
    MODULE=53
    PLUS=54
    MINUSMINUS=55
    MINUS=56
    DIV=57
    MOD=58
    EQUAL_SYMBOL=59
    GREATER_SYMBOL=60
    LESS_SYMBOL=61
    EXCLAMATION_SYMBOL=62
    BIT_NOT_OP=63
    BIT_OR_OP=64
    BIT_AND_OP=65
    BIT_XOR_OP=66
    DOT=67
    LR_BRACKET=68
    RR_BRACKET=69
    COMMA=70
    STRING_LITERAL=71
    DECIMAL_LITERAL=72
    REAL_LITERAL=73
    NULL_SPEC_LITERAL=74
    DOT_ID=75
    ID=76
    ERROR_RECONGNIGION=77

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SelectStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_selectStatement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleSelectContext(SelectStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.SelectStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def querySpecification(self):
            return self.getTypedRuleContext(MySqlParser.QuerySpecificationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleSelect" ):
                listener.enterSimpleSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleSelect" ):
                listener.exitSimpleSelect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleSelect" ):
                return visitor.visitSimpleSelect(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisSelectContext(SelectStatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.SelectStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def queryExpression(self):
            return self.getTypedRuleContext(MySqlParser.QueryExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesisSelect" ):
                listener.enterParenthesisSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesisSelect" ):
                listener.exitParenthesisSelect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisSelect" ):
                return visitor.visitParenthesisSelect(self)
            else:
                return visitor.visitChildren(self)



    def selectStatement(self):

        localctx = MySqlParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_selectStatement)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlParser.SELECT]:
                localctx = MySqlParser.SimpleSelectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.querySpecification()
                pass
            elif token in [MySqlParser.LR_BRACKET]:
                localctx = MySqlParser.ParenthesisSelectContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.queryExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(MySqlParser.ORDER, 0)

        def BY(self):
            return self.getToken(MySqlParser.BY, 0)

        def orderByExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.OrderByExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlParser.OrderByExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_orderByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClause" ):
                listener.enterOrderByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClause" ):
                listener.exitOrderByClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByClause" ):
                return visitor.visitOrderByClause(self)
            else:
                return visitor.visitChildren(self)




    def orderByClause(self):

        localctx = MySqlParser.OrderByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MySqlParser.ORDER)
            self.state = 71
            self.match(MySqlParser.BY)
            self.state = 72
            self.orderByExpression()
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlParser.COMMA:
                self.state = 73
                self.match(MySqlParser.COMMA)
                self.state = 74
                self.orderByExpression()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.order = None # Token

        def expression(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionContext,0)


        def ASC(self):
            return self.getToken(MySqlParser.ASC, 0)

        def DESC(self):
            return self.getToken(MySqlParser.DESC, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_orderByExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByExpression" ):
                listener.enterOrderByExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByExpression" ):
                listener.exitOrderByExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByExpression" ):
                return visitor.visitOrderByExpression(self)
            else:
                return visitor.visitChildren(self)




    def orderByExpression(self):

        localctx = MySqlParser.OrderByExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_orderByExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.expression(0)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.ASC or _la==MySqlParser.DESC:
                self.state = 81
                localctx.order = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MySqlParser.ASC or _la==MySqlParser.DESC):
                    localctx.order = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_tableSource

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TableSourceNestedContext(TableSourceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.TableSourceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def tableSourceItem(self):
            return self.getTypedRuleContext(MySqlParser.TableSourceItemContext,0)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def joinPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.JoinPartContext)
            else:
                return self.getTypedRuleContext(MySqlParser.JoinPartContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSourceNested" ):
                listener.enterTableSourceNested(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSourceNested" ):
                listener.exitTableSourceNested(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSourceNested" ):
                return visitor.visitTableSourceNested(self)
            else:
                return visitor.visitChildren(self)


    class TableSourceBaseContext(TableSourceContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.TableSourceContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tableSourceItem(self):
            return self.getTypedRuleContext(MySqlParser.TableSourceItemContext,0)

        def joinPart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.JoinPartContext)
            else:
                return self.getTypedRuleContext(MySqlParser.JoinPartContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSourceBase" ):
                listener.enterTableSourceBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSourceBase" ):
                listener.exitTableSourceBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSourceBase" ):
                return visitor.visitTableSourceBase(self)
            else:
                return visitor.visitChildren(self)



    def tableSource(self):

        localctx = MySqlParser.TableSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tableSource)
        self._la = 0 # Token type
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = MySqlParser.TableSourceBaseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.tableSourceItem()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.CROSS) | (1 << MySqlParser.INNER) | (1 << MySqlParser.JOIN) | (1 << MySqlParser.LEFT) | (1 << MySqlParser.RIGHT))) != 0):
                    self.state = 85
                    self.joinPart()
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                localctx = MySqlParser.TableSourceNestedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(MySqlParser.LR_BRACKET)
                self.state = 92
                self.tableSourceItem()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.CROSS) | (1 << MySqlParser.INNER) | (1 << MySqlParser.JOIN) | (1 << MySqlParser.LEFT) | (1 << MySqlParser.RIGHT))) != 0):
                    self.state = 93
                    self.joinPart()
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 99
                self.match(MySqlParser.RR_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourcesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableSource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.TableSourceContext)
            else:
                return self.getTypedRuleContext(MySqlParser.TableSourceContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_tableSources

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSources" ):
                listener.enterTableSources(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSources" ):
                listener.exitTableSources(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSources" ):
                return visitor.visitTableSources(self)
            else:
                return visitor.visitChildren(self)




    def tableSources(self):

        localctx = MySqlParser.TableSourcesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tableSources)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.tableSource()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlParser.COMMA:
                self.state = 104
                self.match(MySqlParser.COMMA)
                self.state = 105
                self.tableSource()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourceItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_tableSourceItem

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SubqueryTableItemContext(TableSourceItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.TableSourceItemContext
            super().__init__(parser)
            self.parenthesisSubquery = None # SelectStatementContext
            self.alias = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)
        def selectStatement(self):
            return self.getTypedRuleContext(MySqlParser.SelectStatementContext,0)

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def AS(self):
            return self.getToken(MySqlParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubqueryTableItem" ):
                listener.enterSubqueryTableItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubqueryTableItem" ):
                listener.exitSubqueryTableItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubqueryTableItem" ):
                return visitor.visitSubqueryTableItem(self)
            else:
                return visitor.visitChildren(self)


    class AtomTableItemContext(TableSourceItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.TableSourceItemContext
            super().__init__(parser)
            self.alias = None # Token
            self.copyFrom(ctx)

        def fullId(self):
            return self.getTypedRuleContext(MySqlParser.FullIdContext,0)

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)
        def AS(self):
            return self.getToken(MySqlParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomTableItem" ):
                listener.enterAtomTableItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomTableItem" ):
                listener.exitAtomTableItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomTableItem" ):
                return visitor.visitAtomTableItem(self)
            else:
                return visitor.visitChildren(self)


    class TableSourcesItemContext(TableSourceItemContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.TableSourceItemContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def tableSources(self):
            return self.getTypedRuleContext(MySqlParser.TableSourcesContext,0)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSourcesItem" ):
                listener.enterTableSourcesItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSourcesItem" ):
                listener.exitTableSourcesItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSourcesItem" ):
                return visitor.visitTableSourcesItem(self)
            else:
                return visitor.visitChildren(self)



    def tableSourceItem(self):

        localctx = MySqlParser.TableSourceItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tableSourceItem)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = MySqlParser.AtomTableItemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.fullId()
                self.state = 116
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MySqlParser.AS:
                        self.state = 112
                        self.match(MySqlParser.AS)


                    self.state = 115
                    localctx.alias = self.match(MySqlParser.ID)


                pass

            elif la_ == 2:
                localctx = MySqlParser.SubqueryTableItemContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 118
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 119
                    self.match(MySqlParser.LR_BRACKET)
                    self.state = 120
                    localctx.parenthesisSubquery = self.selectStatement()
                    self.state = 121
                    self.match(MySqlParser.RR_BRACKET)
                    pass


                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlParser.AS:
                    self.state = 125
                    self.match(MySqlParser.AS)


                self.state = 128
                localctx.alias = self.match(MySqlParser.ID)
                pass

            elif la_ == 3:
                localctx = MySqlParser.TableSourcesItemContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 130
                self.match(MySqlParser.LR_BRACKET)
                self.state = 131
                self.tableSources()
                self.state = 132
                self.match(MySqlParser.RR_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinPartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_joinPart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InnerJoinContext(JoinPartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.JoinPartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JOIN(self):
            return self.getToken(MySqlParser.JOIN, 0)
        def tableSourceItem(self):
            return self.getTypedRuleContext(MySqlParser.TableSourceItemContext,0)

        def INNER(self):
            return self.getToken(MySqlParser.INNER, 0)
        def CROSS(self):
            return self.getToken(MySqlParser.CROSS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInnerJoin" ):
                listener.enterInnerJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInnerJoin" ):
                listener.exitInnerJoin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInnerJoin" ):
                return visitor.visitInnerJoin(self)
            else:
                return visitor.visitChildren(self)


    class OuterJoinContext(JoinPartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.JoinPartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JOIN(self):
            return self.getToken(MySqlParser.JOIN, 0)
        def tableSourceItem(self):
            return self.getTypedRuleContext(MySqlParser.TableSourceItemContext,0)

        def LEFT(self):
            return self.getToken(MySqlParser.LEFT, 0)
        def RIGHT(self):
            return self.getToken(MySqlParser.RIGHT, 0)
        def ON(self):
            return self.getToken(MySqlParser.ON, 0)
        def expression(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionContext,0)

        def USING(self):
            return self.getToken(MySqlParser.USING, 0)
        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def uidList(self):
            return self.getTypedRuleContext(MySqlParser.UidListContext,0)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def OUTER(self):
            return self.getToken(MySqlParser.OUTER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOuterJoin" ):
                listener.enterOuterJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOuterJoin" ):
                listener.exitOuterJoin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOuterJoin" ):
                return visitor.visitOuterJoin(self)
            else:
                return visitor.visitChildren(self)



    def joinPart(self):

        localctx = MySqlParser.JoinPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_joinPart)
        self._la = 0 # Token type
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlParser.CROSS, MySqlParser.INNER, MySqlParser.JOIN]:
                localctx = MySqlParser.InnerJoinContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlParser.CROSS or _la==MySqlParser.INNER:
                    self.state = 136
                    _la = self._input.LA(1)
                    if not(_la==MySqlParser.CROSS or _la==MySqlParser.INNER):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                self.state = 139
                self.match(MySqlParser.JOIN)
                self.state = 140
                self.tableSourceItem()
                pass
            elif token in [MySqlParser.LEFT, MySqlParser.RIGHT]:
                localctx = MySqlParser.OuterJoinContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==MySqlParser.LEFT or _la==MySqlParser.RIGHT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlParser.OUTER:
                    self.state = 142
                    self.match(MySqlParser.OUTER)


                self.state = 145
                self.match(MySqlParser.JOIN)
                self.state = 146
                self.tableSourceItem()
                self.state = 154
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MySqlParser.ON]:
                    self.state = 147
                    self.match(MySqlParser.ON)
                    self.state = 148
                    self.expression(0)
                    pass
                elif token in [MySqlParser.USING]:
                    self.state = 149
                    self.match(MySqlParser.USING)
                    self.state = 150
                    self.match(MySqlParser.LR_BRACKET)
                    self.state = 151
                    self.uidList()
                    self.state = 152
                    self.match(MySqlParser.RR_BRACKET)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)

        def querySpecification(self):
            return self.getTypedRuleContext(MySqlParser.QuerySpecificationContext,0)


        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)

        def queryExpression(self):
            return self.getTypedRuleContext(MySqlParser.QueryExpressionContext,0)


        def getRuleIndex(self):
            return MySqlParser.RULE_queryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQueryExpression" ):
                listener.enterQueryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQueryExpression" ):
                listener.exitQueryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQueryExpression" ):
                return visitor.visitQueryExpression(self)
            else:
                return visitor.visitChildren(self)




    def queryExpression(self):

        localctx = MySqlParser.QueryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_queryExpression)
        try:
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(MySqlParser.LR_BRACKET)
                self.state = 159
                self.querySpecification()
                self.state = 160
                self.match(MySqlParser.RR_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(MySqlParser.LR_BRACKET)
                self.state = 163
                self.queryExpression()
                self.state = 164
                self.match(MySqlParser.RR_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuerySpecificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MySqlParser.SELECT, 0)

        def selectElements(self):
            return self.getTypedRuleContext(MySqlParser.SelectElementsContext,0)


        def DISTINCT(self):
            return self.getToken(MySqlParser.DISTINCT, 0)

        def fromClause(self):
            return self.getTypedRuleContext(MySqlParser.FromClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(MySqlParser.OrderByClauseContext,0)


        def limitClause(self):
            return self.getTypedRuleContext(MySqlParser.LimitClauseContext,0)


        def getRuleIndex(self):
            return MySqlParser.RULE_querySpecification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuerySpecification" ):
                listener.enterQuerySpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuerySpecification" ):
                listener.exitQuerySpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuerySpecification" ):
                return visitor.visitQuerySpecification(self)
            else:
                return visitor.visitChildren(self)




    def querySpecification(self):

        localctx = MySqlParser.QuerySpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_querySpecification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MySqlParser.SELECT)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.DISTINCT:
                self.state = 169
                self.match(MySqlParser.DISTINCT)


            self.state = 172
            self.selectElements()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.FROM:
                self.state = 173
                self.fromClause()


            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.ORDER:
                self.state = 176
                self.orderByClause()


            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.LIMIT:
                self.state = 179
                self.limitClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectElementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.star = None # Token

        def selectElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.SelectElementContext)
            else:
                return self.getTypedRuleContext(MySqlParser.SelectElementContext,i)


        def STAR(self):
            return self.getToken(MySqlParser.STAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_selectElements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectElements" ):
                listener.enterSelectElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectElements" ):
                listener.exitSelectElements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectElements" ):
                return visitor.visitSelectElements(self)
            else:
                return visitor.visitChildren(self)




    def selectElements(self):

        localctx = MySqlParser.SelectElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selectElements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlParser.STAR]:
                self.state = 182
                localctx.star = self.match(MySqlParser.STAR)
                pass
            elif token in [MySqlParser.CASE, MySqlParser.EXISTS, MySqlParser.FALSE, MySqlParser.NOT, MySqlParser.NULL_LITERAL, MySqlParser.TRUE, MySqlParser.PLUS, MySqlParser.MINUS, MySqlParser.EXCLAMATION_SYMBOL, MySqlParser.BIT_NOT_OP, MySqlParser.LR_BRACKET, MySqlParser.STRING_LITERAL, MySqlParser.DECIMAL_LITERAL, MySqlParser.REAL_LITERAL, MySqlParser.NULL_SPEC_LITERAL, MySqlParser.ID]:
                self.state = 183
                self.selectElement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlParser.COMMA:
                self.state = 186
                self.match(MySqlParser.COMMA)
                self.state = 187
                self.selectElement()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_selectElement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectExpressionElementContext(SelectElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.SelectElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionContext,0)

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)
        def AS(self):
            return self.getToken(MySqlParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectExpressionElement" ):
                listener.enterSelectExpressionElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectExpressionElement" ):
                listener.exitSelectExpressionElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectExpressionElement" ):
                return visitor.visitSelectExpressionElement(self)
            else:
                return visitor.visitChildren(self)


    class SelectFunctionElementContext(SelectElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.SelectElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(MySqlParser.FunctionCallContext,0)

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)
        def AS(self):
            return self.getToken(MySqlParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectFunctionElement" ):
                listener.enterSelectFunctionElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectFunctionElement" ):
                listener.exitSelectFunctionElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectFunctionElement" ):
                return visitor.visitSelectFunctionElement(self)
            else:
                return visitor.visitChildren(self)


    class SelectColumnElementContext(SelectElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.SelectElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlParser.FullColumnNameContext,0)

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)
        def AS(self):
            return self.getToken(MySqlParser.AS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectColumnElement" ):
                listener.enterSelectColumnElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectColumnElement" ):
                listener.exitSelectColumnElement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectColumnElement" ):
                return visitor.visitSelectColumnElement(self)
            else:
                return visitor.visitChildren(self)



    def selectElement(self):

        localctx = MySqlParser.SelectElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_selectElement)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                localctx = MySqlParser.SelectColumnElementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.fullColumnName()
                self.state = 198
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 195
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MySqlParser.AS:
                        self.state = 194
                        self.match(MySqlParser.AS)


                    self.state = 197
                    self.match(MySqlParser.ID)


                pass

            elif la_ == 2:
                localctx = MySqlParser.SelectFunctionElementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.functionCall()
                self.state = 205
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MySqlParser.AS:
                        self.state = 201
                        self.match(MySqlParser.AS)


                    self.state = 204
                    self.match(MySqlParser.ID)


                pass

            elif la_ == 3:
                localctx = MySqlParser.SelectExpressionElementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.expression(0)
                self.state = 212
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                if la_ == 1:
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MySqlParser.AS:
                        self.state = 208
                        self.match(MySqlParser.AS)


                    self.state = 211
                    self.match(MySqlParser.ID)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.whereExpr = None # ExpressionContext
            self.havingExpr = None # ExpressionContext

        def FROM(self):
            return self.getToken(MySqlParser.FROM, 0)

        def tableSources(self):
            return self.getTypedRuleContext(MySqlParser.TableSourcesContext,0)


        def WHERE(self):
            return self.getToken(MySqlParser.WHERE, 0)

        def GROUP(self):
            return self.getToken(MySqlParser.GROUP, 0)

        def BY(self):
            return self.getToken(MySqlParser.BY, 0)

        def groupByItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.GroupByItemContext)
            else:
                return self.getTypedRuleContext(MySqlParser.GroupByItemContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def HAVING(self):
            return self.getToken(MySqlParser.HAVING, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_fromClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromClause" ):
                listener.enterFromClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromClause" ):
                listener.exitFromClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromClause" ):
                return visitor.visitFromClause(self)
            else:
                return visitor.visitChildren(self)




    def fromClause(self):

        localctx = MySqlParser.FromClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fromClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(MySqlParser.FROM)
            self.state = 217
            self.tableSources()
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.WHERE:
                self.state = 218
                self.match(MySqlParser.WHERE)
                self.state = 219
                localctx.whereExpr = self.expression(0)


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.GROUP:
                self.state = 222
                self.match(MySqlParser.GROUP)
                self.state = 223
                self.match(MySqlParser.BY)
                self.state = 224
                self.groupByItem()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MySqlParser.COMMA:
                    self.state = 225
                    self.match(MySqlParser.COMMA)
                    self.state = 226
                    self.groupByItem()
                    self.state = 231
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlParser.HAVING:
                    self.state = 232
                    self.match(MySqlParser.HAVING)
                    self.state = 233
                    localctx.havingExpr = self.expression(0)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupByItemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.order = None # Token

        def expression(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionContext,0)


        def ASC(self):
            return self.getToken(MySqlParser.ASC, 0)

        def DESC(self):
            return self.getToken(MySqlParser.DESC, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_groupByItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupByItem" ):
                listener.enterGroupByItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupByItem" ):
                listener.exitGroupByItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupByItem" ):
                return visitor.visitGroupByItem(self)
            else:
                return visitor.visitChildren(self)




    def groupByItem(self):

        localctx = MySqlParser.GroupByItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_groupByItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.expression(0)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.ASC or _la==MySqlParser.DESC:
                self.state = 239
                localctx.order = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MySqlParser.ASC or _la==MySqlParser.DESC):
                    localctx.order = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LimitClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.offset = None # Token
            self.limit = None # Token

        def LIMIT(self):
            return self.getToken(MySqlParser.LIMIT, 0)

        def OFFSET(self):
            return self.getToken(MySqlParser.OFFSET, 0)

        def DECIMAL_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.DECIMAL_LITERAL)
            else:
                return self.getToken(MySqlParser.DECIMAL_LITERAL, i)

        def COMMA(self):
            return self.getToken(MySqlParser.COMMA, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_limitClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitClause" ):
                listener.enterLimitClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitClause" ):
                listener.exitLimitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitClause" ):
                return visitor.visitLimitClause(self)
            else:
                return visitor.visitChildren(self)




    def limitClause(self):

        localctx = MySqlParser.LimitClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MySqlParser.LIMIT)
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 245
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 243
                    localctx.offset = self.match(MySqlParser.DECIMAL_LITERAL)
                    self.state = 244
                    self.match(MySqlParser.COMMA)


                self.state = 247
                localctx.limit = self.match(MySqlParser.DECIMAL_LITERAL)
                pass

            elif la_ == 2:
                self.state = 248
                localctx.limit = self.match(MySqlParser.DECIMAL_LITERAL)
                self.state = 249
                self.match(MySqlParser.OFFSET)
                self.state = 250
                localctx.offset = self.match(MySqlParser.DECIMAL_LITERAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)

        def DOT_ID(self):
            return self.getToken(MySqlParser.DOT_ID, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_fullId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullId" ):
                listener.enterFullId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullId" ):
                listener.exitFullId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullId" ):
                return visitor.visitFullId(self)
            else:
                return visitor.visitChildren(self)




    def fullId(self):

        localctx = MySqlParser.FullIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_fullId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MySqlParser.ID)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.DOT_ID:
                self.state = 254
                self.match(MySqlParser.DOT_ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FullColumnNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)

        def DOT_ID(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.DOT_ID)
            else:
                return self.getToken(MySqlParser.DOT_ID, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_fullColumnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullColumnName" ):
                listener.enterFullColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullColumnName" ):
                listener.exitFullColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullColumnName" ):
                return visitor.visitFullColumnName(self)
            else:
                return visitor.visitChildren(self)




    def fullColumnName(self):

        localctx = MySqlParser.FullColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_fullColumnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(MySqlParser.ID)
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 258
                self.match(MySqlParser.DOT_ID)
                self.state = 260
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 259
                    self.match(MySqlParser.DOT_ID)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanLiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(MySqlParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MySqlParser.FALSE, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_booleanLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanLiteral" ):
                listener.enterBooleanLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanLiteral" ):
                listener.exitBooleanLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanLiteral" ):
                return visitor.visitBooleanLiteral(self)
            else:
                return visitor.visitChildren(self)




    def booleanLiteral(self):

        localctx = MySqlParser.BooleanLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_booleanLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            _la = self._input.LA(1)
            if not(_la==MySqlParser.FALSE or _la==MySqlParser.TRUE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullNotnullContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL_LITERAL(self):
            return self.getToken(MySqlParser.NULL_LITERAL, 0)

        def NULL_SPEC_LITERAL(self):
            return self.getToken(MySqlParser.NULL_SPEC_LITERAL, 0)

        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_nullNotnull

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullNotnull" ):
                listener.enterNullNotnull(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullNotnull" ):
                listener.exitNullNotnull(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullNotnull" ):
                return visitor.visitNullNotnull(self)
            else:
                return visitor.visitChildren(self)




    def nullNotnull(self):

        localctx = MySqlParser.NullNotnullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_nullNotnull)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.NOT:
                self.state = 266
                self.match(MySqlParser.NOT)


            self.state = 269
            _la = self._input.LA(1)
            if not(_la==MySqlParser.NULL_LITERAL or _la==MySqlParser.NULL_SPEC_LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.nullLiteral = None # Token

        def STRING_LITERAL(self):
            return self.getToken(MySqlParser.STRING_LITERAL, 0)

        def DECIMAL_LITERAL(self):
            return self.getToken(MySqlParser.DECIMAL_LITERAL, 0)

        def MINUS(self):
            return self.getToken(MySqlParser.MINUS, 0)

        def booleanLiteral(self):
            return self.getTypedRuleContext(MySqlParser.BooleanLiteralContext,0)


        def REAL_LITERAL(self):
            return self.getToken(MySqlParser.REAL_LITERAL, 0)

        def NULL_LITERAL(self):
            return self.getToken(MySqlParser.NULL_LITERAL, 0)

        def NULL_SPEC_LITERAL(self):
            return self.getToken(MySqlParser.NULL_SPEC_LITERAL, 0)

        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = MySqlParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(MySqlParser.STRING_LITERAL)
                pass
            elif token in [MySqlParser.DECIMAL_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.match(MySqlParser.DECIMAL_LITERAL)
                pass
            elif token in [MySqlParser.MINUS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.match(MySqlParser.MINUS)
                self.state = 274
                self.match(MySqlParser.DECIMAL_LITERAL)
                pass
            elif token in [MySqlParser.FALSE, MySqlParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 275
                self.booleanLiteral()
                pass
            elif token in [MySqlParser.REAL_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 276
                self.match(MySqlParser.REAL_LITERAL)
                pass
            elif token in [MySqlParser.NOT, MySqlParser.NULL_LITERAL, MySqlParser.NULL_SPEC_LITERAL]:
                self.enterOuterAlt(localctx, 6)
                self.state = 278
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlParser.NOT:
                    self.state = 277
                    self.match(MySqlParser.NOT)


                self.state = 280
                localctx.nullLiteral = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MySqlParser.NULL_LITERAL or _la==MySqlParser.NULL_SPEC_LITERAL):
                    localctx.nullLiteral = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UidListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.ID)
            else:
                return self.getToken(MySqlParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_uidList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUidList" ):
                listener.enterUidList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUidList" ):
                listener.exitUidList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUidList" ):
                return visitor.visitUidList(self)
            else:
                return visitor.visitChildren(self)




    def uidList(self):

        localctx = MySqlParser.UidListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_uidList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(MySqlParser.ID)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlParser.COMMA:
                self.state = 284
                self.match(MySqlParser.COMMA)
                self.state = 285
                self.match(MySqlParser.ID)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressions" ):
                listener.enterExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressions" ):
                listener.exitExpressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = MySqlParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.expression(0)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlParser.COMMA:
                self.state = 292
                self.match(MySqlParser.COMMA)
                self.state = 293
                self.expression(0)
                self.state = 298
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SpecificFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def specificFunction(self):
            return self.getTypedRuleContext(MySqlParser.SpecificFunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecificFunctionCall" ):
                listener.enterSpecificFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecificFunctionCall" ):
                listener.exitSpecificFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificFunctionCall" ):
                return visitor.visitSpecificFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class ScalarFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(MySqlParser.ID, 0)
        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def functionArgs(self):
            return self.getTypedRuleContext(MySqlParser.FunctionArgsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScalarFunctionCall" ):
                listener.enterScalarFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScalarFunctionCall" ):
                listener.exitScalarFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalarFunctionCall" ):
                return visitor.visitScalarFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = MySqlParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MySqlParser.CASE]:
                localctx = MySqlParser.SpecificFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.specificFunction()
                pass
            elif token in [MySqlParser.ID]:
                localctx = MySqlParser.ScalarFunctionCallContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(MySqlParser.ID)
                self.state = 301
                self.match(MySqlParser.LR_BRACKET)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.ALL) | (1 << MySqlParser.CASE) | (1 << MySqlParser.EXISTS) | (1 << MySqlParser.FALSE) | (1 << MySqlParser.NOT) | (1 << MySqlParser.NULL_LITERAL) | (1 << MySqlParser.TRUE) | (1 << MySqlParser.STAR) | (1 << MySqlParser.PLUS) | (1 << MySqlParser.MINUS) | (1 << MySqlParser.EXCLAMATION_SYMBOL) | (1 << MySqlParser.BIT_NOT_OP))) != 0) or ((((_la - 68)) & ~0x3f) == 0 and ((1 << (_la - 68)) & ((1 << (MySqlParser.LR_BRACKET - 68)) | (1 << (MySqlParser.STRING_LITERAL - 68)) | (1 << (MySqlParser.DECIMAL_LITERAL - 68)) | (1 << (MySqlParser.REAL_LITERAL - 68)) | (1 << (MySqlParser.NULL_SPEC_LITERAL - 68)) | (1 << (MySqlParser.ID - 68)))) != 0):
                    self.state = 302
                    self.functionArgs()


                self.state = 305
                self.match(MySqlParser.RR_BRACKET)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecificFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_specificFunction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CaseFunctionCallContext(SpecificFunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.SpecificFunctionContext
            super().__init__(parser)
            self.elseArg = None # FunctionArgContext
            self.copyFrom(ctx)

        def CASE(self):
            return self.getToken(MySqlParser.CASE, 0)
        def END(self):
            return self.getToken(MySqlParser.END, 0)
        def caseFuncAlternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.CaseFuncAlternativeContext)
            else:
                return self.getTypedRuleContext(MySqlParser.CaseFuncAlternativeContext,i)

        def ELSE(self):
            return self.getToken(MySqlParser.ELSE, 0)
        def functionArg(self):
            return self.getTypedRuleContext(MySqlParser.FunctionArgContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseFunctionCall" ):
                listener.enterCaseFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseFunctionCall" ):
                listener.exitCaseFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseFunctionCall" ):
                return visitor.visitCaseFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def specificFunction(self):

        localctx = MySqlParser.SpecificFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_specificFunction)
        self._la = 0 # Token type
        try:
            localctx = MySqlParser.CaseFunctionCallContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(MySqlParser.CASE)
            self.state = 310 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 309
                self.caseFuncAlternative()
                self.state = 312 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MySqlParser.WHEN):
                    break

            self.state = 316
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MySqlParser.ELSE:
                self.state = 314
                self.match(MySqlParser.ELSE)
                self.state = 315
                localctx.elseArg = self.functionArg()


            self.state = 318
            self.match(MySqlParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseFuncAlternativeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # FunctionArgContext
            self.consequent = None # FunctionArgContext

        def WHEN(self):
            return self.getToken(MySqlParser.WHEN, 0)

        def THEN(self):
            return self.getToken(MySqlParser.THEN, 0)

        def functionArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.FunctionArgContext)
            else:
                return self.getTypedRuleContext(MySqlParser.FunctionArgContext,i)


        def getRuleIndex(self):
            return MySqlParser.RULE_caseFuncAlternative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseFuncAlternative" ):
                listener.enterCaseFuncAlternative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseFuncAlternative" ):
                listener.exitCaseFuncAlternative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseFuncAlternative" ):
                return visitor.visitCaseFuncAlternative(self)
            else:
                return visitor.visitChildren(self)




    def caseFuncAlternative(self):

        localctx = MySqlParser.CaseFuncAlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_caseFuncAlternative)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(MySqlParser.WHEN)
            self.state = 321
            localctx.condition = self.functionArg()
            self.state = 322
            self.match(MySqlParser.THEN)
            self.state = 323
            localctx.consequent = self.functionArg()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.STAR)
            else:
                return self.getToken(MySqlParser.STAR, i)

        def ALL(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.ALL)
            else:
                return self.getToken(MySqlParser.ALL, i)

        def constant(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ConstantContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ConstantContext,i)


        def fullColumnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.FullColumnNameContext)
            else:
                return self.getTypedRuleContext(MySqlParser.FullColumnNameContext,i)


        def functionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.FunctionCallContext)
            else:
                return self.getTypedRuleContext(MySqlParser.FunctionCallContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def getRuleIndex(self):
            return MySqlParser.RULE_functionArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgs" ):
                listener.enterFunctionArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgs" ):
                listener.exitFunctionArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgs" ):
                return visitor.visitFunctionArgs(self)
            else:
                return visitor.visitChildren(self)




    def functionArgs(self):

        localctx = MySqlParser.FunctionArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_functionArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 325
                self.match(MySqlParser.STAR)
                pass

            elif la_ == 2:
                self.state = 326
                self.match(MySqlParser.ALL)
                pass

            elif la_ == 3:
                self.state = 327
                self.constant()
                pass

            elif la_ == 4:
                self.state = 328
                self.fullColumnName()
                pass

            elif la_ == 5:
                self.state = 329
                self.functionCall()
                pass

            elif la_ == 6:
                self.state = 330
                self.expression(0)
                pass


            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MySqlParser.COMMA:
                self.state = 333
                self.match(MySqlParser.COMMA)
                self.state = 340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
                if la_ == 1:
                    self.state = 334
                    self.match(MySqlParser.STAR)
                    pass

                elif la_ == 2:
                    self.state = 335
                    self.match(MySqlParser.ALL)
                    pass

                elif la_ == 3:
                    self.state = 336
                    self.constant()
                    pass

                elif la_ == 4:
                    self.state = 337
                    self.fullColumnName()
                    pass

                elif la_ == 5:
                    self.state = 338
                    self.functionCall()
                    pass

                elif la_ == 6:
                    self.state = 339
                    self.expression(0)
                    pass


                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(MySqlParser.ConstantContext,0)


        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlParser.FullColumnNameContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MySqlParser.FunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MySqlParser.RULE_functionArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArg" ):
                listener.enterFunctionArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArg" ):
                listener.exitFunctionArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArg" ):
                return visitor.visitFunctionArg(self)
            else:
                return visitor.visitChildren(self)




    def functionArg(self):

        localctx = MySqlParser.FunctionArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionArg)
        try:
            self.state = 351
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.fullColumnName()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 350
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IsExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionContext
            super().__init__(parser)
            self.testValue = None # Token
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlParser.PredicateContext,0)

        def IS(self):
            return self.getToken(MySqlParser.IS, 0)
        def TRUE(self):
            return self.getToken(MySqlParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(MySqlParser.FALSE, 0)
        def UNKNOWN(self):
            return self.getToken(MySqlParser.UNKNOWN, 0)
        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsExpression" ):
                listener.enterIsExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsExpression" ):
                listener.exitIsExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsExpression" ):
                return visitor.visitIsExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionContext
            super().__init__(parser)
            self.notOperator = None # Token
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionContext,0)

        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)
        def EXCLAMATION_SYMBOL(self):
            return self.getToken(MySqlParser.EXCLAMATION_SYMBOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionContext,i)

        def logicalOperator(self):
            return self.getTypedRuleContext(MySqlParser.LogicalOperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpression" ):
                listener.enterLogicalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpression" ):
                listener.exitLogicalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpression" ):
                return visitor.visitLogicalExpression(self)
            else:
                return visitor.visitChildren(self)


    class PredicateExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlParser.PredicateContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPredicateExpression" ):
                listener.enterPredicateExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPredicateExpression" ):
                listener.exitPredicateExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredicateExpression" ):
                return visitor.visitPredicateExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MySqlParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                localctx = MySqlParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 354
                localctx.notOperator = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==MySqlParser.NOT or _la==MySqlParser.EXCLAMATION_SYMBOL):
                    localctx.notOperator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 355
                self.expression(4)
                pass

            elif la_ == 2:
                localctx = MySqlParser.IsExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 356
                self.predicate(0)
                self.state = 357
                self.match(MySqlParser.IS)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MySqlParser.NOT:
                    self.state = 358
                    self.match(MySqlParser.NOT)


                self.state = 361
                localctx.testValue = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.FALSE) | (1 << MySqlParser.TRUE) | (1 << MySqlParser.UNKNOWN))) != 0)):
                    localctx.testValue = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = MySqlParser.PredicateExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 363
                self.predicate(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,55,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MySqlParser.LogicalExpressionContext(self, MySqlParser.ExpressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 366
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 367
                    self.logicalOperator()
                    self.state = 368
                    self.expression(4) 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,55,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PredicateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_predicate

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExpressionAtomPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressionAtom(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionAtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionAtomPredicate" ):
                listener.enterExpressionAtomPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionAtomPredicate" ):
                listener.exitExpressionAtomPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionAtomPredicate" ):
                return visitor.visitExpressionAtomPredicate(self)
            else:
                return visitor.visitChildren(self)


    class InPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlParser.PredicateContext,0)

        def IN(self):
            return self.getToken(MySqlParser.IN, 0)
        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def selectStatement(self):
            return self.getTypedRuleContext(MySqlParser.SelectStatementContext,0)

        def expressions(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionsContext,0)

        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInPredicate" ):
                listener.enterInPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInPredicate" ):
                listener.exitInPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInPredicate" ):
                return visitor.visitInPredicate(self)
            else:
                return visitor.visitChildren(self)


    class SubqueryComparasionPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.quantifier = None # Token
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlParser.PredicateContext,0)

        def comparisonOperator(self):
            return self.getTypedRuleContext(MySqlParser.ComparisonOperatorContext,0)

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def selectStatement(self):
            return self.getTypedRuleContext(MySqlParser.SelectStatementContext,0)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def ALL(self):
            return self.getToken(MySqlParser.ALL, 0)
        def ANY(self):
            return self.getToken(MySqlParser.ANY, 0)
        def SOME(self):
            return self.getToken(MySqlParser.SOME, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubqueryComparasionPredicate" ):
                listener.enterSubqueryComparasionPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubqueryComparasionPredicate" ):
                listener.exitSubqueryComparasionPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubqueryComparasionPredicate" ):
                return visitor.visitSubqueryComparasionPredicate(self)
            else:
                return visitor.visitChildren(self)


    class BetweenPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlParser.PredicateContext,i)

        def BETWEEN(self):
            return self.getToken(MySqlParser.BETWEEN, 0)
        def AND(self):
            return self.getToken(MySqlParser.AND, 0)
        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetweenPredicate" ):
                listener.enterBetweenPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetweenPredicate" ):
                listener.exitBetweenPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenPredicate" ):
                return visitor.visitBetweenPredicate(self)
            else:
                return visitor.visitChildren(self)


    class BinaryComparasionPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.left = None # PredicateContext
            self.right = None # PredicateContext
            self.copyFrom(ctx)

        def comparisonOperator(self):
            return self.getTypedRuleContext(MySqlParser.ComparisonOperatorContext,0)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlParser.PredicateContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryComparasionPredicate" ):
                listener.enterBinaryComparasionPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryComparasionPredicate" ):
                listener.exitBinaryComparasionPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryComparasionPredicate" ):
                return visitor.visitBinaryComparasionPredicate(self)
            else:
                return visitor.visitChildren(self)


    class IsNullPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self):
            return self.getTypedRuleContext(MySqlParser.PredicateContext,0)

        def IS(self):
            return self.getToken(MySqlParser.IS, 0)
        def nullNotnull(self):
            return self.getTypedRuleContext(MySqlParser.NullNotnullContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsNullPredicate" ):
                listener.enterIsNullPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsNullPredicate" ):
                listener.exitIsNullPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsNullPredicate" ):
                return visitor.visitIsNullPredicate(self)
            else:
                return visitor.visitChildren(self)


    class LikePredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlParser.PredicateContext,i)

        def LIKE(self):
            return self.getToken(MySqlParser.LIKE, 0)
        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLikePredicate" ):
                listener.enterLikePredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLikePredicate" ):
                listener.exitLikePredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLikePredicate" ):
                return visitor.visitLikePredicate(self)
            else:
                return visitor.visitChildren(self)


    class RegexpPredicateContext(PredicateContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.PredicateContext
            super().__init__(parser)
            self.regex = None # Token
            self.copyFrom(ctx)

        def predicate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.PredicateContext)
            else:
                return self.getTypedRuleContext(MySqlParser.PredicateContext,i)

        def REGEXP(self):
            return self.getToken(MySqlParser.REGEXP, 0)
        def RLIKE(self):
            return self.getToken(MySqlParser.RLIKE, 0)
        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegexpPredicate" ):
                listener.enterRegexpPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegexpPredicate" ):
                listener.exitRegexpPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexpPredicate" ):
                return visitor.visitRegexpPredicate(self)
            else:
                return visitor.visitChildren(self)



    def predicate(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MySqlParser.PredicateContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_predicate, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MySqlParser.ExpressionAtomPredicateContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 376
            self.expressionAtom(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 425
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        localctx = MySqlParser.BinaryComparasionPredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 378
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 379
                        self.comparisonOperator()
                        self.state = 380
                        localctx.right = self.predicate(7)
                        pass

                    elif la_ == 2:
                        localctx = MySqlParser.BetweenPredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 382
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 384
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MySqlParser.NOT:
                            self.state = 383
                            self.match(MySqlParser.NOT)


                        self.state = 386
                        self.match(MySqlParser.BETWEEN)
                        self.state = 387
                        self.predicate(0)
                        self.state = 388
                        self.match(MySqlParser.AND)
                        self.state = 389
                        self.predicate(5)
                        pass

                    elif la_ == 3:
                        localctx = MySqlParser.LikePredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 391
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 393
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MySqlParser.NOT:
                            self.state = 392
                            self.match(MySqlParser.NOT)


                        self.state = 395
                        self.match(MySqlParser.LIKE)
                        self.state = 396
                        self.predicate(4)
                        pass

                    elif la_ == 4:
                        localctx = MySqlParser.RegexpPredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 397
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 399
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MySqlParser.NOT:
                            self.state = 398
                            self.match(MySqlParser.NOT)


                        self.state = 401
                        localctx.regex = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==MySqlParser.REGEXP or _la==MySqlParser.RLIKE):
                            localctx.regex = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 402
                        self.predicate(3)
                        pass

                    elif la_ == 5:
                        localctx = MySqlParser.InPredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 403
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 405
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MySqlParser.NOT:
                            self.state = 404
                            self.match(MySqlParser.NOT)


                        self.state = 407
                        self.match(MySqlParser.IN)
                        self.state = 408
                        self.match(MySqlParser.LR_BRACKET)
                        self.state = 411
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                        if la_ == 1:
                            self.state = 409
                            self.selectStatement()
                            pass

                        elif la_ == 2:
                            self.state = 410
                            self.expressions()
                            pass


                        self.state = 413
                        self.match(MySqlParser.RR_BRACKET)
                        pass

                    elif la_ == 6:
                        localctx = MySqlParser.IsNullPredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 415
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 416
                        self.match(MySqlParser.IS)
                        self.state = 417
                        self.nullNotnull()
                        pass

                    elif la_ == 7:
                        localctx = MySqlParser.SubqueryComparasionPredicateContext(self, MySqlParser.PredicateContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_predicate)
                        self.state = 418
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 419
                        self.comparisonOperator()
                        self.state = 420
                        localctx.quantifier = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.ALL) | (1 << MySqlParser.ANY) | (1 << MySqlParser.SOME))) != 0)):
                            localctx.quantifier = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 421
                        self.match(MySqlParser.LR_BRACKET)
                        self.state = 422
                        self.selectStatement()
                        self.state = 423
                        self.match(MySqlParser.RR_BRACKET)
                        pass

             
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionAtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MySqlParser.RULE_expressionAtom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class UnaryExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryOperator(self):
            return self.getTypedRuleContext(MySqlParser.UnaryOperatorContext,0)

        def expressionAtom(self):
            return self.getTypedRuleContext(MySqlParser.ExpressionAtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpressionAtom" ):
                listener.enterUnaryExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpressionAtom" ):
                listener.exitUnaryExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpressionAtom" ):
                return visitor.visitUnaryExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class SubqueryExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def selectStatement(self):
            return self.getTypedRuleContext(MySqlParser.SelectStatementContext,0)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubqueryExpressionAtom" ):
                listener.enterSubqueryExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubqueryExpressionAtom" ):
                listener.exitSubqueryExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubqueryExpressionAtom" ):
                return visitor.visitSubqueryExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class PriorityMathExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.left = None # ExpressionAtomContext
            self.op = None # Token
            self.right = None # ExpressionAtomContext
            self.copyFrom(ctx)

        def expressionAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionAtomContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionAtomContext,i)

        def STAR(self):
            return self.getToken(MySqlParser.STAR, 0)
        def DIVIDE(self):
            return self.getToken(MySqlParser.DIVIDE, 0)
        def MODULE(self):
            return self.getToken(MySqlParser.MODULE, 0)
        def DIV(self):
            return self.getToken(MySqlParser.DIV, 0)
        def MOD(self):
            return self.getToken(MySqlParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPriorityMathExpressionAtom" ):
                listener.enterPriorityMathExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPriorityMathExpressionAtom" ):
                listener.exitPriorityMathExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPriorityMathExpressionAtom" ):
                return visitor.visitPriorityMathExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class ConstantExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(MySqlParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpressionAtom" ):
                listener.enterConstantExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpressionAtom" ):
                listener.exitConstantExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantExpressionAtom" ):
                return visitor.visitConstantExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(MySqlParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpressionAtom" ):
                listener.enterFunctionCallExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpressionAtom" ):
                listener.exitFunctionCallExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpressionAtom" ):
                return visitor.visitFunctionCallExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class FullColumnNameExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fullColumnName(self):
            return self.getTypedRuleContext(MySqlParser.FullColumnNameContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFullColumnNameExpressionAtom" ):
                listener.enterFullColumnNameExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFullColumnNameExpressionAtom" ):
                listener.exitFullColumnNameExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFullColumnNameExpressionAtom" ):
                return visitor.visitFullColumnNameExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class NestedExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionContext,i)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MySqlParser.COMMA)
            else:
                return self.getToken(MySqlParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNestedExpressionAtom" ):
                listener.enterNestedExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNestedExpressionAtom" ):
                listener.exitNestedExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedExpressionAtom" ):
                return visitor.visitNestedExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class MathExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.left = None # ExpressionAtomContext
            self.right = None # ExpressionAtomContext
            self.copyFrom(ctx)

        def mathOperator(self):
            return self.getTypedRuleContext(MySqlParser.MathOperatorContext,0)

        def expressionAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MySqlParser.ExpressionAtomContext)
            else:
                return self.getTypedRuleContext(MySqlParser.ExpressionAtomContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathExpressionAtom" ):
                listener.enterMathExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathExpressionAtom" ):
                listener.exitMathExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathExpressionAtom" ):
                return visitor.visitMathExpressionAtom(self)
            else:
                return visitor.visitChildren(self)


    class ExistsExpressionAtomContext(ExpressionAtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MySqlParser.ExpressionAtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXISTS(self):
            return self.getToken(MySqlParser.EXISTS, 0)
        def LR_BRACKET(self):
            return self.getToken(MySqlParser.LR_BRACKET, 0)
        def selectStatement(self):
            return self.getTypedRuleContext(MySqlParser.SelectStatementContext,0)

        def RR_BRACKET(self):
            return self.getToken(MySqlParser.RR_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExistsExpressionAtom" ):
                listener.enterExistsExpressionAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExistsExpressionAtom" ):
                listener.exitExistsExpressionAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExistsExpressionAtom" ):
                return visitor.visitExistsExpressionAtom(self)
            else:
                return visitor.visitChildren(self)



    def expressionAtom(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MySqlParser.ExpressionAtomContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expressionAtom, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                localctx = MySqlParser.ConstantExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 431
                self.constant()
                pass

            elif la_ == 2:
                localctx = MySqlParser.FullColumnNameExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 432
                self.fullColumnName()
                pass

            elif la_ == 3:
                localctx = MySqlParser.FunctionCallExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 433
                self.functionCall()
                pass

            elif la_ == 4:
                localctx = MySqlParser.UnaryExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 434
                self.unaryOperator()
                self.state = 435
                self.expressionAtom(6)
                pass

            elif la_ == 5:
                localctx = MySqlParser.NestedExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 437
                self.match(MySqlParser.LR_BRACKET)
                self.state = 438
                self.expression(0)
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MySqlParser.COMMA:
                    self.state = 439
                    self.match(MySqlParser.COMMA)
                    self.state = 440
                    self.expression(0)
                    self.state = 445
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 446
                self.match(MySqlParser.RR_BRACKET)
                pass

            elif la_ == 6:
                localctx = MySqlParser.ExistsExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 448
                self.match(MySqlParser.EXISTS)
                self.state = 449
                self.match(MySqlParser.LR_BRACKET)
                self.state = 450
                self.selectStatement()
                self.state = 451
                self.match(MySqlParser.RR_BRACKET)
                pass

            elif la_ == 7:
                localctx = MySqlParser.SubqueryExpressionAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 453
                self.match(MySqlParser.LR_BRACKET)
                self.state = 454
                self.selectStatement()
                self.state = 455
                self.match(MySqlParser.RR_BRACKET)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,66,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 466
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
                    if la_ == 1:
                        localctx = MySqlParser.PriorityMathExpressionAtomContext(self, MySqlParser.ExpressionAtomContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionAtom)
                        self.state = 459
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 460
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.STAR) | (1 << MySqlParser.DIVIDE) | (1 << MySqlParser.MODULE) | (1 << MySqlParser.DIV) | (1 << MySqlParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 461
                        localctx.right = self.expressionAtom(3)
                        pass

                    elif la_ == 2:
                        localctx = MySqlParser.MathExpressionAtomContext(self, MySqlParser.ExpressionAtomContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressionAtom)
                        self.state = 462
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 463
                        self.mathOperator()
                        self.state = 464
                        localctx.right = self.expressionAtom(2)
                        pass

             
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,66,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCLAMATION_SYMBOL(self):
            return self.getToken(MySqlParser.EXCLAMATION_SYMBOL, 0)

        def BIT_NOT_OP(self):
            return self.getToken(MySqlParser.BIT_NOT_OP, 0)

        def PLUS(self):
            return self.getToken(MySqlParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MySqlParser.MINUS, 0)

        def NOT(self):
            return self.getToken(MySqlParser.NOT, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_unaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOperator" ):
                listener.enterUnaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOperator" ):
                listener.exitUnaryOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOperator" ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def unaryOperator(self):

        localctx = MySqlParser.UnaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_unaryOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.NOT) | (1 << MySqlParser.PLUS) | (1 << MySqlParser.MINUS) | (1 << MySqlParser.EXCLAMATION_SYMBOL) | (1 << MySqlParser.BIT_NOT_OP))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL_SYMBOL(self):
            return self.getToken(MySqlParser.EQUAL_SYMBOL, 0)

        def GREATER_SYMBOL(self):
            return self.getToken(MySqlParser.GREATER_SYMBOL, 0)

        def LESS_SYMBOL(self):
            return self.getToken(MySqlParser.LESS_SYMBOL, 0)

        def EXCLAMATION_SYMBOL(self):
            return self.getToken(MySqlParser.EXCLAMATION_SYMBOL, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = MySqlParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_comparisonOperator)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(MySqlParser.EQUAL_SYMBOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.match(MySqlParser.GREATER_SYMBOL)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 475
                self.match(MySqlParser.LESS_SYMBOL)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 476
                self.match(MySqlParser.LESS_SYMBOL)
                self.state = 477
                self.match(MySqlParser.EQUAL_SYMBOL)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 478
                self.match(MySqlParser.GREATER_SYMBOL)
                self.state = 479
                self.match(MySqlParser.EQUAL_SYMBOL)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 480
                self.match(MySqlParser.LESS_SYMBOL)
                self.state = 481
                self.match(MySqlParser.GREATER_SYMBOL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 482
                self.match(MySqlParser.EXCLAMATION_SYMBOL)
                self.state = 483
                self.match(MySqlParser.EQUAL_SYMBOL)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 484
                self.match(MySqlParser.LESS_SYMBOL)
                self.state = 485
                self.match(MySqlParser.EQUAL_SYMBOL)
                self.state = 486
                self.match(MySqlParser.GREATER_SYMBOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(MySqlParser.AND, 0)

        def OR(self):
            return self.getToken(MySqlParser.OR, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_logicalOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOperator" ):
                listener.enterLogicalOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOperator" ):
                listener.exitLogicalOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOperator" ):
                return visitor.visitLogicalOperator(self)
            else:
                return visitor.visitChildren(self)




    def logicalOperator(self):

        localctx = MySqlParser.LogicalOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_logicalOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            _la = self._input.LA(1)
            if not(_la==MySqlParser.AND or _la==MySqlParser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MathOperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(MySqlParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MySqlParser.MINUS, 0)

        def MINUSMINUS(self):
            return self.getToken(MySqlParser.MINUSMINUS, 0)

        def getRuleIndex(self):
            return MySqlParser.RULE_mathOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathOperator" ):
                listener.enterMathOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathOperator" ):
                listener.exitMathOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOperator" ):
                return visitor.visitMathOperator(self)
            else:
                return visitor.visitChildren(self)




    def mathOperator(self):

        localctx = MySqlParser.MathOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_mathOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MySqlParser.PLUS) | (1 << MySqlParser.MINUSMINUS) | (1 << MySqlParser.MINUS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expression_sempred
        self._predicates[27] = self.predicate_sempred
        self._predicates[28] = self.expressionAtom_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def predicate_sempred(self, localctx:PredicateContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

    def expressionAtom_sempred(self, localctx:ExpressionAtomContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




