# Generated from /Users/zhangzhiqiang/PycharmProjects/PyLinq/PyLinq/parser/MySqlLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2O")
        buf.write("\u026a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\6\2\u00a9")
        buf.write("\n\2\r\2\16\2\u00aa\3\2\3\2\3\3\3\3\3\3\3\3\3\3\6\3\u00b4")
        buf.write("\n\3\r\3\16\3\u00b5\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u00c1\n\4\f\4\16\4\u00c4\13\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\5\5\u00cf\n\5\3\5\7\5\u00d2\n\5\f\5")
        buf.write("\16\5\u00d5\13\5\3\5\5\5\u00d8\n\5\3\5\3\5\5\5\u00dc\n")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5\u00e2\n\5\3\5\3\5\5\5\u00e6\n\5")
        buf.write("\5\5\u00e8\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\38\39\39\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\3G\3G\3H\3H\5H\u0211\nH\3I\6I\u0214\nI\r")
        buf.write("I\16I\u0215\3J\6J\u0219\nJ\rJ\16J\u021a\5J\u021d\nJ\3")
        buf.write("J\3J\6J\u0221\nJ\rJ\16J\u0222\3K\3K\3K\3L\3L\3L\3M\3M")
        buf.write("\3N\7N\u022e\nN\fN\16N\u0231\13N\3N\6N\u0234\nN\rN\16")
        buf.write("N\u0235\3N\7N\u0239\nN\fN\16N\u023c\13N\3O\3O\3O\3O\3")
        buf.write("O\3O\7O\u0244\nO\fO\16O\u0247\13O\3O\3O\3P\3P\3P\3P\3")
        buf.write("P\3P\7P\u0251\nP\fP\16P\u0254\13P\3P\3P\3Q\3Q\3Q\3Q\3")
        buf.write("Q\3Q\7Q\u025e\nQ\fQ\16Q\u0261\13Q\3Q\3Q\3R\3R\3S\3S\3")
        buf.write("S\3S\6\u00b5\u00c2\u022f\u0235\2T\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009b\2\u009d\2\u009f\2")
        buf.write("\u00a1\2\u00a3\2\u00a5O\3\2\n\5\2\13\f\17\17\"\"\4\2\f")
        buf.write("\f\17\17\7\2&&\62;C\\aac|\6\2&&C\\aac|\4\2$$^^\4\2))^")
        buf.write("^\4\2^^bb\3\2\62;\2\u027f\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\3\u00a8\3\2\2\2\5\u00ae\3\2\2\2\7\u00bc\3\2\2")
        buf.write("\2\t\u00e7\3\2\2\2\13\u00eb\3\2\2\2\r\u00ef\3\2\2\2\17")
        buf.write("\u00f3\3\2\2\2\21\u00f6\3\2\2\2\23\u00fa\3\2\2\2\25\u0102")
        buf.write("\3\2\2\2\27\u0105\3\2\2\2\31\u010a\3\2\2\2\33\u0110\3")
        buf.write("\2\2\2\35\u0115\3\2\2\2\37\u011e\3\2\2\2!\u0123\3\2\2")
        buf.write("\2#\u012a\3\2\2\2%\u0130\3\2\2\2\'\u0135\3\2\2\2)\u013b")
        buf.write("\3\2\2\2+\u0142\3\2\2\2-\u0145\3\2\2\2/\u014b\3\2\2\2")
        buf.write("\61\u0150\3\2\2\2\63\u0153\3\2\2\2\65\u0158\3\2\2\2\67")
        buf.write("\u015d\3\2\2\29\u0162\3\2\2\2;\u0168\3\2\2\2=\u016c\3")
        buf.write("\2\2\2?\u0171\3\2\2\2A\u0174\3\2\2\2C\u0177\3\2\2\2E\u017d")
        buf.write("\3\2\2\2G\u0183\3\2\2\2I\u018a\3\2\2\2K\u0190\3\2\2\2")
        buf.write("M\u0196\3\2\2\2O\u019d\3\2\2\2Q\u01a2\3\2\2\2S\u01a7\3")
        buf.write("\2\2\2U\u01ad\3\2\2\2W\u01b3\3\2\2\2Y\u01ba\3\2\2\2[\u01bf")
        buf.write("\3\2\2\2]\u01c5\3\2\2\2_\u01c9\3\2\2\2a\u01cd\3\2\2\2")
        buf.write("c\u01d4\3\2\2\2e\u01d9\3\2\2\2g\u01e1\3\2\2\2i\u01e3\3")
        buf.write("\2\2\2k\u01e5\3\2\2\2m\u01e7\3\2\2\2o\u01e9\3\2\2\2q\u01ec")
        buf.write("\3\2\2\2s\u01ee\3\2\2\2u\u01f2\3\2\2\2w\u01f6\3\2\2\2")
        buf.write("y\u01f8\3\2\2\2{\u01fa\3\2\2\2}\u01fc\3\2\2\2\177\u01fe")
        buf.write("\3\2\2\2\u0081\u0200\3\2\2\2\u0083\u0202\3\2\2\2\u0085")
        buf.write("\u0204\3\2\2\2\u0087\u0206\3\2\2\2\u0089\u0208\3\2\2\2")
        buf.write("\u008b\u020a\3\2\2\2\u008d\u020c\3\2\2\2\u008f\u0210\3")
        buf.write("\2\2\2\u0091\u0213\3\2\2\2\u0093\u021c\3\2\2\2\u0095\u0224")
        buf.write("\3\2\2\2\u0097\u0227\3\2\2\2\u0099\u022a\3\2\2\2\u009b")
        buf.write("\u022f\3\2\2\2\u009d\u023d\3\2\2\2\u009f\u024a\3\2\2\2")
        buf.write("\u00a1\u0257\3\2\2\2\u00a3\u0264\3\2\2\2\u00a5\u0266\3")
        buf.write("\2\2\2\u00a7\u00a9\t\2\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ad\b\2\2\2\u00ad\4\3\2\2\2\u00ae")
        buf.write("\u00af\7\61\2\2\u00af\u00b0\7,\2\2\u00b0\u00b1\7#\2\2")
        buf.write("\u00b1\u00b3\3\2\2\2\u00b2\u00b4\13\2\2\2\u00b3\u00b2")
        buf.write("\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\7,\2\2")
        buf.write("\u00b8\u00b9\7\61\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb")
        buf.write("\b\3\3\2\u00bb\6\3\2\2\2\u00bc\u00bd\7\61\2\2\u00bd\u00be")
        buf.write("\7,\2\2\u00be\u00c2\3\2\2\2\u00bf\u00c1\13\2\2\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2\u00c3\3\2\2\2")
        buf.write("\u00c2\u00c0\3\2\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00c2\3")
        buf.write("\2\2\2\u00c5\u00c6\7,\2\2\u00c6\u00c7\7\61\2\2\u00c7\u00c8")
        buf.write("\3\2\2\2\u00c8\u00c9\b\4\2\2\u00c9\b\3\2\2\2\u00ca\u00cb")
        buf.write("\7/\2\2\u00cb\u00cc\7/\2\2\u00cc\u00cf\7\"\2\2\u00cd\u00cf")
        buf.write("\7%\2\2\u00ce\u00ca\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d3\3\2\2\2\u00d0\u00d2\n\3\2\2\u00d1\u00d0\3\2\2\2")
        buf.write("\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3")
        buf.write("\2\2\2\u00d4\u00db\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d8")
        buf.write("\7\17\2\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00dc\7\f\2\2\u00da\u00dc\7\2\2\3")
        buf.write("\u00db\u00d7\3\2\2\2\u00db\u00da\3\2\2\2\u00dc\u00e8\3")
        buf.write("\2\2\2\u00dd\u00de\7/\2\2\u00de\u00df\7/\2\2\u00df\u00e5")
        buf.write("\3\2\2\2\u00e0\u00e2\7\17\2\2\u00e1\u00e0\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e6\7\f\2\2")
        buf.write("\u00e4\u00e6\7\2\2\3\u00e5\u00e1\3\2\2\2\u00e5\u00e4\3")
        buf.write("\2\2\2\u00e6\u00e8\3\2\2\2\u00e7\u00ce\3\2\2\2\u00e7\u00dd")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\b\5\2\2\u00ea")
        buf.write("\n\3\2\2\2\u00eb\u00ec\7C\2\2\u00ec\u00ed\7N\2\2\u00ed")
        buf.write("\u00ee\7N\2\2\u00ee\f\3\2\2\2\u00ef\u00f0\7C\2\2\u00f0")
        buf.write("\u00f1\7P\2\2\u00f1\u00f2\7F\2\2\u00f2\16\3\2\2\2\u00f3")
        buf.write("\u00f4\7C\2\2\u00f4\u00f5\7U\2\2\u00f5\20\3\2\2\2\u00f6")
        buf.write("\u00f7\7C\2\2\u00f7\u00f8\7U\2\2\u00f8\u00f9\7E\2\2\u00f9")
        buf.write("\22\3\2\2\2\u00fa\u00fb\7D\2\2\u00fb\u00fc\7G\2\2\u00fc")
        buf.write("\u00fd\7V\2\2\u00fd\u00fe\7Y\2\2\u00fe\u00ff\7G\2\2\u00ff")
        buf.write("\u0100\7G\2\2\u0100\u0101\7P\2\2\u0101\24\3\2\2\2\u0102")
        buf.write("\u0103\7D\2\2\u0103\u0104\7[\2\2\u0104\26\3\2\2\2\u0105")
        buf.write("\u0106\7E\2\2\u0106\u0107\7C\2\2\u0107\u0108\7U\2\2\u0108")
        buf.write("\u0109\7G\2\2\u0109\30\3\2\2\2\u010a\u010b\7E\2\2\u010b")
        buf.write("\u010c\7T\2\2\u010c\u010d\7Q\2\2\u010d\u010e\7U\2\2\u010e")
        buf.write("\u010f\7U\2\2\u010f\32\3\2\2\2\u0110\u0111\7F\2\2\u0111")
        buf.write("\u0112\7G\2\2\u0112\u0113\7U\2\2\u0113\u0114\7E\2\2\u0114")
        buf.write("\34\3\2\2\2\u0115\u0116\7F\2\2\u0116\u0117\7K\2\2\u0117")
        buf.write("\u0118\7U\2\2\u0118\u0119\7V\2\2\u0119\u011a\7K\2\2\u011a")
        buf.write("\u011b\7P\2\2\u011b\u011c\7E\2\2\u011c\u011d\7V\2\2\u011d")
        buf.write("\36\3\2\2\2\u011e\u011f\7G\2\2\u011f\u0120\7N\2\2\u0120")
        buf.write("\u0121\7U\2\2\u0121\u0122\7G\2\2\u0122 \3\2\2\2\u0123")
        buf.write("\u0124\7G\2\2\u0124\u0125\7Z\2\2\u0125\u0126\7K\2\2\u0126")
        buf.write("\u0127\7U\2\2\u0127\u0128\7V\2\2\u0128\u0129\7U\2\2\u0129")
        buf.write("\"\3\2\2\2\u012a\u012b\7H\2\2\u012b\u012c\7C\2\2\u012c")
        buf.write("\u012d\7N\2\2\u012d\u012e\7U\2\2\u012e\u012f\7G\2\2\u012f")
        buf.write("$\3\2\2\2\u0130\u0131\7H\2\2\u0131\u0132\7T\2\2\u0132")
        buf.write("\u0133\7Q\2\2\u0133\u0134\7O\2\2\u0134&\3\2\2\2\u0135")
        buf.write("\u0136\7I\2\2\u0136\u0137\7T\2\2\u0137\u0138\7Q\2\2\u0138")
        buf.write("\u0139\7W\2\2\u0139\u013a\7R\2\2\u013a(\3\2\2\2\u013b")
        buf.write("\u013c\7J\2\2\u013c\u013d\7C\2\2\u013d\u013e\7X\2\2\u013e")
        buf.write("\u013f\7K\2\2\u013f\u0140\7P\2\2\u0140\u0141\7I\2\2\u0141")
        buf.write("*\3\2\2\2\u0142\u0143\7K\2\2\u0143\u0144\7P\2\2\u0144")
        buf.write(",\3\2\2\2\u0145\u0146\7K\2\2\u0146\u0147\7P\2\2\u0147")
        buf.write("\u0148\7P\2\2\u0148\u0149\7G\2\2\u0149\u014a\7T\2\2\u014a")
        buf.write(".\3\2\2\2\u014b\u014c\7K\2\2\u014c\u014d\7P\2\2\u014d")
        buf.write("\u014e\7V\2\2\u014e\u014f\7Q\2\2\u014f\60\3\2\2\2\u0150")
        buf.write("\u0151\7K\2\2\u0151\u0152\7U\2\2\u0152\62\3\2\2\2\u0153")
        buf.write("\u0154\7L\2\2\u0154\u0155\7Q\2\2\u0155\u0156\7K\2\2\u0156")
        buf.write("\u0157\7P\2\2\u0157\64\3\2\2\2\u0158\u0159\7N\2\2\u0159")
        buf.write("\u015a\7G\2\2\u015a\u015b\7H\2\2\u015b\u015c\7V\2\2\u015c")
        buf.write("\66\3\2\2\2\u015d\u015e\7N\2\2\u015e\u015f\7K\2\2\u015f")
        buf.write("\u0160\7M\2\2\u0160\u0161\7G\2\2\u01618\3\2\2\2\u0162")
        buf.write("\u0163\7N\2\2\u0163\u0164\7K\2\2\u0164\u0165\7O\2\2\u0165")
        buf.write("\u0166\7K\2\2\u0166\u0167\7V\2\2\u0167:\3\2\2\2\u0168")
        buf.write("\u0169\7P\2\2\u0169\u016a\7Q\2\2\u016a\u016b\7V\2\2\u016b")
        buf.write("<\3\2\2\2\u016c\u016d\7P\2\2\u016d\u016e\7W\2\2\u016e")
        buf.write("\u016f\7N\2\2\u016f\u0170\7N\2\2\u0170>\3\2\2\2\u0171")
        buf.write("\u0172\7Q\2\2\u0172\u0173\7P\2\2\u0173@\3\2\2\2\u0174")
        buf.write("\u0175\7Q\2\2\u0175\u0176\7T\2\2\u0176B\3\2\2\2\u0177")
        buf.write("\u0178\7Q\2\2\u0178\u0179\7T\2\2\u0179\u017a\7F\2\2\u017a")
        buf.write("\u017b\7G\2\2\u017b\u017c\7T\2\2\u017cD\3\2\2\2\u017d")
        buf.write("\u017e\7Q\2\2\u017e\u017f\7W\2\2\u017f\u0180\7V\2\2\u0180")
        buf.write("\u0181\7G\2\2\u0181\u0182\7T\2\2\u0182F\3\2\2\2\u0183")
        buf.write("\u0184\7T\2\2\u0184\u0185\7G\2\2\u0185\u0186\7I\2\2\u0186")
        buf.write("\u0187\7G\2\2\u0187\u0188\7Z\2\2\u0188\u0189\7R\2\2\u0189")
        buf.write("H\3\2\2\2\u018a\u018b\7T\2\2\u018b\u018c\7K\2\2\u018c")
        buf.write("\u018d\7I\2\2\u018d\u018e\7J\2\2\u018e\u018f\7V\2\2\u018f")
        buf.write("J\3\2\2\2\u0190\u0191\7T\2\2\u0191\u0192\7N\2\2\u0192")
        buf.write("\u0193\7K\2\2\u0193\u0194\7M\2\2\u0194\u0195\7G\2\2\u0195")
        buf.write("L\3\2\2\2\u0196\u0197\7U\2\2\u0197\u0198\7G\2\2\u0198")
        buf.write("\u0199\7N\2\2\u0199\u019a\7G\2\2\u019a\u019b\7E\2\2\u019b")
        buf.write("\u019c\7V\2\2\u019cN\3\2\2\2\u019d\u019e\7V\2\2\u019e")
        buf.write("\u019f\7J\2\2\u019f\u01a0\7G\2\2\u01a0\u01a1\7P\2\2\u01a1")
        buf.write("P\3\2\2\2\u01a2\u01a3\7V\2\2\u01a3\u01a4\7T\2\2\u01a4")
        buf.write("\u01a5\7W\2\2\u01a5\u01a6\7G\2\2\u01a6R\3\2\2\2\u01a7")
        buf.write("\u01a8\7W\2\2\u01a8\u01a9\7P\2\2\u01a9\u01aa\7K\2\2\u01aa")
        buf.write("\u01ab\7Q\2\2\u01ab\u01ac\7P\2\2\u01acT\3\2\2\2\u01ad")
        buf.write("\u01ae\7W\2\2\u01ae\u01af\7U\2\2\u01af\u01b0\7K\2\2\u01b0")
        buf.write("\u01b1\7P\2\2\u01b1\u01b2\7I\2\2\u01b2V\3\2\2\2\u01b3")
        buf.write("\u01b4\7X\2\2\u01b4\u01b5\7C\2\2\u01b5\u01b6\7N\2\2\u01b6")
        buf.write("\u01b7\7W\2\2\u01b7\u01b8\7G\2\2\u01b8\u01b9\7U\2\2\u01b9")
        buf.write("X\3\2\2\2\u01ba\u01bb\7Y\2\2\u01bb\u01bc\7J\2\2\u01bc")
        buf.write("\u01bd\7G\2\2\u01bd\u01be\7P\2\2\u01beZ\3\2\2\2\u01bf")
        buf.write("\u01c0\7Y\2\2\u01c0\u01c1\7J\2\2\u01c1\u01c2\7G\2\2\u01c2")
        buf.write("\u01c3\7T\2\2\u01c3\u01c4\7G\2\2\u01c4\\\3\2\2\2\u01c5")
        buf.write("\u01c6\7C\2\2\u01c6\u01c7\7P\2\2\u01c7\u01c8\7[\2\2\u01c8")
        buf.write("^\3\2\2\2\u01c9\u01ca\7G\2\2\u01ca\u01cb\7P\2\2\u01cb")
        buf.write("\u01cc\7F\2\2\u01cc`\3\2\2\2\u01cd\u01ce\7Q\2\2\u01ce")
        buf.write("\u01cf\7H\2\2\u01cf\u01d0\7H\2\2\u01d0\u01d1\7U\2\2\u01d1")
        buf.write("\u01d2\7G\2\2\u01d2\u01d3\7V\2\2\u01d3b\3\2\2\2\u01d4")
        buf.write("\u01d5\7U\2\2\u01d5\u01d6\7Q\2\2\u01d6\u01d7\7O\2\2\u01d7")
        buf.write("\u01d8\7G\2\2\u01d8d\3\2\2\2\u01d9\u01da\7W\2\2\u01da")
        buf.write("\u01db\7P\2\2\u01db\u01dc\7M\2\2\u01dc\u01dd\7P\2\2\u01dd")
        buf.write("\u01de\7Q\2\2\u01de\u01df\7Y\2\2\u01df\u01e0\7P\2\2\u01e0")
        buf.write("f\3\2\2\2\u01e1\u01e2\7,\2\2\u01e2h\3\2\2\2\u01e3\u01e4")
        buf.write("\7\61\2\2\u01e4j\3\2\2\2\u01e5\u01e6\7\'\2\2\u01e6l\3")
        buf.write("\2\2\2\u01e7\u01e8\7-\2\2\u01e8n\3\2\2\2\u01e9\u01ea\7")
        buf.write("/\2\2\u01ea\u01eb\7/\2\2\u01ebp\3\2\2\2\u01ec\u01ed\7")
        buf.write("/\2\2\u01edr\3\2\2\2\u01ee\u01ef\7F\2\2\u01ef\u01f0\7")
        buf.write("K\2\2\u01f0\u01f1\7X\2\2\u01f1t\3\2\2\2\u01f2\u01f3\7")
        buf.write("O\2\2\u01f3\u01f4\7Q\2\2\u01f4\u01f5\7F\2\2\u01f5v\3\2")
        buf.write("\2\2\u01f6\u01f7\7?\2\2\u01f7x\3\2\2\2\u01f8\u01f9\7@")
        buf.write("\2\2\u01f9z\3\2\2\2\u01fa\u01fb\7>\2\2\u01fb|\3\2\2\2")
        buf.write("\u01fc\u01fd\7#\2\2\u01fd~\3\2\2\2\u01fe\u01ff\7\u0080")
        buf.write("\2\2\u01ff\u0080\3\2\2\2\u0200\u0201\7~\2\2\u0201\u0082")
        buf.write("\3\2\2\2\u0202\u0203\7(\2\2\u0203\u0084\3\2\2\2\u0204")
        buf.write("\u0205\7`\2\2\u0205\u0086\3\2\2\2\u0206\u0207\7\60\2\2")
        buf.write("\u0207\u0088\3\2\2\2\u0208\u0209\7*\2\2\u0209\u008a\3")
        buf.write("\2\2\2\u020a\u020b\7+\2\2\u020b\u008c\3\2\2\2\u020c\u020d")
        buf.write("\7.\2\2\u020d\u008e\3\2\2\2\u020e\u0211\5\u009dO\2\u020f")
        buf.write("\u0211\5\u009fP\2\u0210\u020e\3\2\2\2\u0210\u020f\3\2")
        buf.write("\2\2\u0211\u0090\3\2\2\2\u0212\u0214\5\u00a3R\2\u0213")
        buf.write("\u0212\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0215\u0216\3\2\2\2\u0216\u0092\3\2\2\2\u0217\u0219\5")
        buf.write("\u00a3R\2\u0218\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3\2\2\2")
        buf.write("\u021c\u0218\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u0220\7\60\2\2\u021f\u0221\5\u00a3R\2\u0220")
        buf.write("\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0220\3\2\2\2")
        buf.write("\u0222\u0223\3\2\2\2\u0223\u0094\3\2\2\2\u0224\u0225\7")
        buf.write("^\2\2\u0225\u0226\7P\2\2\u0226\u0096\3\2\2\2\u0227\u0228")
        buf.write("\7\60\2\2\u0228\u0229\5\u009bN\2\u0229\u0098\3\2\2\2\u022a")
        buf.write("\u022b\5\u009bN\2\u022b\u009a\3\2\2\2\u022c\u022e\t\4")
        buf.write("\2\2\u022d\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u0230")
        buf.write("\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0233\3\2\2\2\u0231")
        buf.write("\u022f\3\2\2\2\u0232\u0234\t\5\2\2\u0233\u0232\3\2\2\2")
        buf.write("\u0234\u0235\3\2\2\2\u0235\u0236\3\2\2\2\u0235\u0233\3")
        buf.write("\2\2\2\u0236\u023a\3\2\2\2\u0237\u0239\t\4\2\2\u0238\u0237")
        buf.write("\3\2\2\2\u0239\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a")
        buf.write("\u023b\3\2\2\2\u023b\u009c\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023d\u0245\7$\2\2\u023e\u023f\7^\2\2\u023f\u0244\13")
        buf.write("\2\2\2\u0240\u0241\7$\2\2\u0241\u0244\7$\2\2\u0242\u0244")
        buf.write("\n\6\2\2\u0243\u023e\3\2\2\2\u0243\u0240\3\2\2\2\u0243")
        buf.write("\u0242\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243\3\2\2\2")
        buf.write("\u0245\u0246\3\2\2\2\u0246\u0248\3\2\2\2\u0247\u0245\3")
        buf.write("\2\2\2\u0248\u0249\7$\2\2\u0249\u009e\3\2\2\2\u024a\u0252")
        buf.write("\7)\2\2\u024b\u024c\7^\2\2\u024c\u0251\13\2\2\2\u024d")
        buf.write("\u024e\7)\2\2\u024e\u0251\7)\2\2\u024f\u0251\n\7\2\2\u0250")
        buf.write("\u024b\3\2\2\2\u0250\u024d\3\2\2\2\u0250\u024f\3\2\2\2")
        buf.write("\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253\3")
        buf.write("\2\2\2\u0253\u0255\3\2\2\2\u0254\u0252\3\2\2\2\u0255\u0256")
        buf.write("\7)\2\2\u0256\u00a0\3\2\2\2\u0257\u025f\7b\2\2\u0258\u0259")
        buf.write("\7^\2\2\u0259\u025e\13\2\2\2\u025a\u025b\7b\2\2\u025b")
        buf.write("\u025e\7b\2\2\u025c\u025e\n\b\2\2\u025d\u0258\3\2\2\2")
        buf.write("\u025d\u025a\3\2\2\2\u025d\u025c\3\2\2\2\u025e\u0261\3")
        buf.write("\2\2\2\u025f\u025d\3\2\2\2\u025f\u0260\3\2\2\2\u0260\u0262")
        buf.write("\3\2\2\2\u0261\u025f\3\2\2\2\u0262\u0263\7b\2\2\u0263")
        buf.write("\u00a2\3\2\2\2\u0264\u0265\t\t\2\2\u0265\u00a4\3\2\2\2")
        buf.write("\u0266\u0267\13\2\2\2\u0267\u0268\3\2\2\2\u0268\u0269")
        buf.write("\bS\4\2\u0269\u00a6\3\2\2\2\33\2\u00aa\u00b5\u00c2\u00ce")
        buf.write("\u00d3\u00d7\u00db\u00e1\u00e5\u00e7\u0210\u0215\u021a")
        buf.write("\u021c\u0222\u022f\u0235\u023a\u0243\u0245\u0250\u0252")
        buf.write("\u025d\u025f\5\2\3\2\2\4\2\2\5\2")
        return buf.getvalue()


class MySqlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MYSQLCOMMENT = 2
    ERRORCHANNEL = 3

    SPACE = 1
    SPEC_MYSQL_COMMENT = 2
    COMMENT_INPUT = 3
    LINE_COMMENT = 4
    ALL = 5
    AND = 6
    AS = 7
    ASC = 8
    BETWEEN = 9
    BY = 10
    CASE = 11
    CROSS = 12
    DESC = 13
    DISTINCT = 14
    ELSE = 15
    EXISTS = 16
    FALSE = 17
    FROM = 18
    GROUP = 19
    HAVING = 20
    IN = 21
    INNER = 22
    INTO = 23
    IS = 24
    JOIN = 25
    LEFT = 26
    LIKE = 27
    LIMIT = 28
    NOT = 29
    NULL_LITERAL = 30
    ON = 31
    OR = 32
    ORDER = 33
    OUTER = 34
    REGEXP = 35
    RIGHT = 36
    RLIKE = 37
    SELECT = 38
    THEN = 39
    TRUE = 40
    UNION = 41
    USING = 42
    VALUES = 43
    WHEN = 44
    WHERE = 45
    ANY = 46
    END = 47
    OFFSET = 48
    SOME = 49
    UNKNOWN = 50
    STAR = 51
    DIVIDE = 52
    MODULE = 53
    PLUS = 54
    MINUSMINUS = 55
    MINUS = 56
    DIV = 57
    MOD = 58
    EQUAL_SYMBOL = 59
    GREATER_SYMBOL = 60
    LESS_SYMBOL = 61
    EXCLAMATION_SYMBOL = 62
    BIT_NOT_OP = 63
    BIT_OR_OP = 64
    BIT_AND_OP = 65
    BIT_XOR_OP = 66
    DOT = 67
    LR_BRACKET = 68
    RR_BRACKET = 69
    COMMA = 70
    STRING_LITERAL = 71
    DECIMAL_LITERAL = 72
    REAL_LITERAL = 73
    NULL_SPEC_LITERAL = 74
    DOT_ID = 75
    ID = 76
    ERROR_RECONGNIGION = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"MYSQLCOMMENT", 
                                                          u"ERRORCHANNEL" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ALL'", "'AND'", "'AS'", "'ASC'", "'BETWEEN'", "'BY'", "'CASE'", 
            "'CROSS'", "'DESC'", "'DISTINCT'", "'ELSE'", "'EXISTS'", "'FALSE'", 
            "'FROM'", "'GROUP'", "'HAVING'", "'IN'", "'INNER'", "'INTO'", 
            "'IS'", "'JOIN'", "'LEFT'", "'LIKE'", "'LIMIT'", "'NOT'", "'NULL'", 
            "'ON'", "'OR'", "'ORDER'", "'OUTER'", "'REGEXP'", "'RIGHT'", 
            "'RLIKE'", "'SELECT'", "'THEN'", "'TRUE'", "'UNION'", "'USING'", 
            "'VALUES'", "'WHEN'", "'WHERE'", "'ANY'", "'END'", "'OFFSET'", 
            "'SOME'", "'UNKNOWN'", "'*'", "'/'", "'%'", "'+'", "'--'", "'-'", 
            "'DIV'", "'MOD'", "'='", "'>'", "'<'", "'!'", "'~'", "'|'", 
            "'&'", "'^'", "'.'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "SPEC_MYSQL_COMMENT", "COMMENT_INPUT", "LINE_COMMENT", 
            "ALL", "AND", "AS", "ASC", "BETWEEN", "BY", "CASE", "CROSS", 
            "DESC", "DISTINCT", "ELSE", "EXISTS", "FALSE", "FROM", "GROUP", 
            "HAVING", "IN", "INNER", "INTO", "IS", "JOIN", "LEFT", "LIKE", 
            "LIMIT", "NOT", "NULL_LITERAL", "ON", "OR", "ORDER", "OUTER", 
            "REGEXP", "RIGHT", "RLIKE", "SELECT", "THEN", "TRUE", "UNION", 
            "USING", "VALUES", "WHEN", "WHERE", "ANY", "END", "OFFSET", 
            "SOME", "UNKNOWN", "STAR", "DIVIDE", "MODULE", "PLUS", "MINUSMINUS", 
            "MINUS", "DIV", "MOD", "EQUAL_SYMBOL", "GREATER_SYMBOL", "LESS_SYMBOL", 
            "EXCLAMATION_SYMBOL", "BIT_NOT_OP", "BIT_OR_OP", "BIT_AND_OP", 
            "BIT_XOR_OP", "DOT", "LR_BRACKET", "RR_BRACKET", "COMMA", "STRING_LITERAL", 
            "DECIMAL_LITERAL", "REAL_LITERAL", "NULL_SPEC_LITERAL", "DOT_ID", 
            "ID", "ERROR_RECONGNIGION" ]

    ruleNames = [ "SPACE", "SPEC_MYSQL_COMMENT", "COMMENT_INPUT", "LINE_COMMENT", 
                  "ALL", "AND", "AS", "ASC", "BETWEEN", "BY", "CASE", "CROSS", 
                  "DESC", "DISTINCT", "ELSE", "EXISTS", "FALSE", "FROM", 
                  "GROUP", "HAVING", "IN", "INNER", "INTO", "IS", "JOIN", 
                  "LEFT", "LIKE", "LIMIT", "NOT", "NULL_LITERAL", "ON", 
                  "OR", "ORDER", "OUTER", "REGEXP", "RIGHT", "RLIKE", "SELECT", 
                  "THEN", "TRUE", "UNION", "USING", "VALUES", "WHEN", "WHERE", 
                  "ANY", "END", "OFFSET", "SOME", "UNKNOWN", "STAR", "DIVIDE", 
                  "MODULE", "PLUS", "MINUSMINUS", "MINUS", "DIV", "MOD", 
                  "EQUAL_SYMBOL", "GREATER_SYMBOL", "LESS_SYMBOL", "EXCLAMATION_SYMBOL", 
                  "BIT_NOT_OP", "BIT_OR_OP", "BIT_AND_OP", "BIT_XOR_OP", 
                  "DOT", "LR_BRACKET", "RR_BRACKET", "COMMA", "STRING_LITERAL", 
                  "DECIMAL_LITERAL", "REAL_LITERAL", "NULL_SPEC_LITERAL", 
                  "DOT_ID", "ID", "ID_LITERAL", "DQUOTA_STRING", "SQUOTA_STRING", 
                  "BQUOTA_STRING", "DEC_DIGIT", "ERROR_RECONGNIGION" ]

    grammarFileName = "MySqlLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


