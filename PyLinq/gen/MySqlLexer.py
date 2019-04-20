# Generated from /Users/zhangzhiqiang/PycharmProjects/PyLinq/PyLinq/parser/MySqlLexer.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2P")
        buf.write("\u0271\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\6\2\u00ab\n\2\r\2\16\2\u00ac\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\6\3\u00b6\n\3\r\3\16\3\u00b7\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\7\4\u00c3\n\4\f\4\16\4\u00c6\13\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5\u00d1\n\5\3\5\7\5")
        buf.write("\u00d4\n\5\f\5\16\5\u00d7\13\5\3\5\5\5\u00da\n\5\3\5\3")
        buf.write("\5\5\5\u00de\n\5\3\5\3\5\3\5\3\5\5\5\u00e4\n\5\3\5\3\5")
        buf.write("\5\5\u00e8\n\5\5\5\u00ea\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write("\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\3:")
        buf.write("\3:\3;\3;\3;\3;\3<\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\5")
        buf.write("I\u0218\nI\3J\6J\u021b\nJ\rJ\16J\u021c\3K\6K\u0220\nK")
        buf.write("\rK\16K\u0221\5K\u0224\nK\3K\3K\6K\u0228\nK\rK\16K\u0229")
        buf.write("\3L\3L\3L\3M\3M\3M\3N\3N\3O\7O\u0235\nO\fO\16O\u0238\13")
        buf.write("O\3O\6O\u023b\nO\rO\16O\u023c\3O\7O\u0240\nO\fO\16O\u0243")
        buf.write("\13O\3P\3P\3P\3P\3P\3P\7P\u024b\nP\fP\16P\u024e\13P\3")
        buf.write("P\3P\3Q\3Q\3Q\3Q\3Q\3Q\7Q\u0258\nQ\fQ\16Q\u025b\13Q\3")
        buf.write("Q\3Q\3R\3R\3R\3R\3R\3R\7R\u0265\nR\fR\16R\u0268\13R\3")
        buf.write("R\3R\3S\3S\3T\3T\3T\3T\6\u00b7\u00c4\u0236\u023c\2U\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008b")
        buf.write("G\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009b")
        buf.write("O\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7P\3\2\n")
        buf.write("\5\2\13\f\17\17\"\"\4\2\f\f\17\17\7\2&&\62;C\\aac|\6\2")
        buf.write("&&C\\aac|\4\2$$^^\4\2))^^\4\2^^bb\3\2\62;\2\u0286\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u00a7\3\2\2\2\3\u00aa")
        buf.write("\3\2\2\2\5\u00b0\3\2\2\2\7\u00be\3\2\2\2\t\u00e9\3\2\2")
        buf.write("\2\13\u00ed\3\2\2\2\r\u00f1\3\2\2\2\17\u00f5\3\2\2\2\21")
        buf.write("\u00f8\3\2\2\2\23\u00fc\3\2\2\2\25\u0104\3\2\2\2\27\u0109")
        buf.write("\3\2\2\2\31\u010c\3\2\2\2\33\u0111\3\2\2\2\35\u0117\3")
        buf.write("\2\2\2\37\u011c\3\2\2\2!\u0125\3\2\2\2#\u012a\3\2\2\2")
        buf.write("%\u0131\3\2\2\2\'\u0137\3\2\2\2)\u013c\3\2\2\2+\u0142")
        buf.write("\3\2\2\2-\u0149\3\2\2\2/\u014c\3\2\2\2\61\u0152\3\2\2")
        buf.write("\2\63\u0157\3\2\2\2\65\u015a\3\2\2\2\67\u015f\3\2\2\2")
        buf.write("9\u0164\3\2\2\2;\u0169\3\2\2\2=\u016f\3\2\2\2?\u0173\3")
        buf.write("\2\2\2A\u0178\3\2\2\2C\u017b\3\2\2\2E\u017e\3\2\2\2G\u0184")
        buf.write("\3\2\2\2I\u018a\3\2\2\2K\u0191\3\2\2\2M\u0197\3\2\2\2")
        buf.write("O\u019d\3\2\2\2Q\u01a4\3\2\2\2S\u01a9\3\2\2\2U\u01ae\3")
        buf.write("\2\2\2W\u01b4\3\2\2\2Y\u01ba\3\2\2\2[\u01c1\3\2\2\2]\u01c6")
        buf.write("\3\2\2\2_\u01cc\3\2\2\2a\u01d0\3\2\2\2c\u01d4\3\2\2\2")
        buf.write("e\u01db\3\2\2\2g\u01e0\3\2\2\2i\u01e8\3\2\2\2k\u01ea\3")
        buf.write("\2\2\2m\u01ec\3\2\2\2o\u01ee\3\2\2\2q\u01f0\3\2\2\2s\u01f3")
        buf.write("\3\2\2\2u\u01f5\3\2\2\2w\u01f9\3\2\2\2y\u01fd\3\2\2\2")
        buf.write("{\u01ff\3\2\2\2}\u0201\3\2\2\2\177\u0203\3\2\2\2\u0081")
        buf.write("\u0205\3\2\2\2\u0083\u0207\3\2\2\2\u0085\u0209\3\2\2\2")
        buf.write("\u0087\u020b\3\2\2\2\u0089\u020d\3\2\2\2\u008b\u020f\3")
        buf.write("\2\2\2\u008d\u0211\3\2\2\2\u008f\u0213\3\2\2\2\u0091\u0217")
        buf.write("\3\2\2\2\u0093\u021a\3\2\2\2\u0095\u0223\3\2\2\2\u0097")
        buf.write("\u022b\3\2\2\2\u0099\u022e\3\2\2\2\u009b\u0231\3\2\2\2")
        buf.write("\u009d\u0236\3\2\2\2\u009f\u0244\3\2\2\2\u00a1\u0251\3")
        buf.write("\2\2\2\u00a3\u025e\3\2\2\2\u00a5\u026b\3\2\2\2\u00a7\u026d")
        buf.write("\3\2\2\2\u00a9\u00ab\t\2\2\2\u00aa\u00a9\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00ae\3\2\2\2\u00ae\u00af\b\2\2\2\u00af\4\3\2\2")
        buf.write("\2\u00b0\u00b1\7\61\2\2\u00b1\u00b2\7,\2\2\u00b2\u00b3")
        buf.write("\7#\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00b6\13\2\2\2\u00b5")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\7")
        buf.write(",\2\2\u00ba\u00bb\7\61\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd")
        buf.write("\b\3\3\2\u00bd\6\3\2\2\2\u00be\u00bf\7\61\2\2\u00bf\u00c0")
        buf.write("\7,\2\2\u00c0\u00c4\3\2\2\2\u00c1\u00c3\13\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3")
        buf.write("\2\2\2\u00c7\u00c8\7,\2\2\u00c8\u00c9\7\61\2\2\u00c9\u00ca")
        buf.write("\3\2\2\2\u00ca\u00cb\b\4\2\2\u00cb\b\3\2\2\2\u00cc\u00cd")
        buf.write("\7/\2\2\u00cd\u00ce\7/\2\2\u00ce\u00d1\7\"\2\2\u00cf\u00d1")
        buf.write("\7%\2\2\u00d0\u00cc\3\2\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d5\3\2\2\2\u00d2\u00d4\n\3\2\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3")
        buf.write("\2\2\2\u00d6\u00dd\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00da")
        buf.write("\7\17\2\2\u00d9\u00d8\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00de\7\f\2\2\u00dc\u00de\7\2\2\3")
        buf.write("\u00dd\u00d9\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\u00ea\3")
        buf.write("\2\2\2\u00df\u00e0\7/\2\2\u00e0\u00e1\7/\2\2\u00e1\u00e7")
        buf.write("\3\2\2\2\u00e2\u00e4\7\17\2\2\u00e3\u00e2\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e8\7\f\2\2")
        buf.write("\u00e6\u00e8\7\2\2\3\u00e7\u00e3\3\2\2\2\u00e7\u00e6\3")
        buf.write("\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00d0\3\2\2\2\u00e9\u00df")
        buf.write("\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\b\5\2\2\u00ec")
        buf.write("\n\3\2\2\2\u00ed\u00ee\7C\2\2\u00ee\u00ef\7N\2\2\u00ef")
        buf.write("\u00f0\7N\2\2\u00f0\f\3\2\2\2\u00f1\u00f2\7C\2\2\u00f2")
        buf.write("\u00f3\7P\2\2\u00f3\u00f4\7F\2\2\u00f4\16\3\2\2\2\u00f5")
        buf.write("\u00f6\7C\2\2\u00f6\u00f7\7U\2\2\u00f7\20\3\2\2\2\u00f8")
        buf.write("\u00f9\7C\2\2\u00f9\u00fa\7U\2\2\u00fa\u00fb\7E\2\2\u00fb")
        buf.write("\22\3\2\2\2\u00fc\u00fd\7D\2\2\u00fd\u00fe\7G\2\2\u00fe")
        buf.write("\u00ff\7V\2\2\u00ff\u0100\7Y\2\2\u0100\u0101\7G\2\2\u0101")
        buf.write("\u0102\7G\2\2\u0102\u0103\7P\2\2\u0103\24\3\2\2\2\u0104")
        buf.write("\u0105\7Y\2\2\u0105\u0106\7K\2\2\u0106\u0107\7V\2\2\u0107")
        buf.write("\u0108\7J\2\2\u0108\26\3\2\2\2\u0109\u010a\7D\2\2\u010a")
        buf.write("\u010b\7[\2\2\u010b\30\3\2\2\2\u010c\u010d\7E\2\2\u010d")
        buf.write("\u010e\7C\2\2\u010e\u010f\7U\2\2\u010f\u0110\7G\2\2\u0110")
        buf.write("\32\3\2\2\2\u0111\u0112\7E\2\2\u0112\u0113\7T\2\2\u0113")
        buf.write("\u0114\7Q\2\2\u0114\u0115\7U\2\2\u0115\u0116\7U\2\2\u0116")
        buf.write("\34\3\2\2\2\u0117\u0118\7F\2\2\u0118\u0119\7G\2\2\u0119")
        buf.write("\u011a\7U\2\2\u011a\u011b\7E\2\2\u011b\36\3\2\2\2\u011c")
        buf.write("\u011d\7F\2\2\u011d\u011e\7K\2\2\u011e\u011f\7U\2\2\u011f")
        buf.write("\u0120\7V\2\2\u0120\u0121\7K\2\2\u0121\u0122\7P\2\2\u0122")
        buf.write("\u0123\7E\2\2\u0123\u0124\7V\2\2\u0124 \3\2\2\2\u0125")
        buf.write("\u0126\7G\2\2\u0126\u0127\7N\2\2\u0127\u0128\7U\2\2\u0128")
        buf.write("\u0129\7G\2\2\u0129\"\3\2\2\2\u012a\u012b\7G\2\2\u012b")
        buf.write("\u012c\7Z\2\2\u012c\u012d\7K\2\2\u012d\u012e\7U\2\2\u012e")
        buf.write("\u012f\7V\2\2\u012f\u0130\7U\2\2\u0130$\3\2\2\2\u0131")
        buf.write("\u0132\7H\2\2\u0132\u0133\7C\2\2\u0133\u0134\7N\2\2\u0134")
        buf.write("\u0135\7U\2\2\u0135\u0136\7G\2\2\u0136&\3\2\2\2\u0137")
        buf.write("\u0138\7H\2\2\u0138\u0139\7T\2\2\u0139\u013a\7Q\2\2\u013a")
        buf.write("\u013b\7O\2\2\u013b(\3\2\2\2\u013c\u013d\7I\2\2\u013d")
        buf.write("\u013e\7T\2\2\u013e\u013f\7Q\2\2\u013f\u0140\7W\2\2\u0140")
        buf.write("\u0141\7R\2\2\u0141*\3\2\2\2\u0142\u0143\7J\2\2\u0143")
        buf.write("\u0144\7C\2\2\u0144\u0145\7X\2\2\u0145\u0146\7K\2\2\u0146")
        buf.write("\u0147\7P\2\2\u0147\u0148\7I\2\2\u0148,\3\2\2\2\u0149")
        buf.write("\u014a\7K\2\2\u014a\u014b\7P\2\2\u014b.\3\2\2\2\u014c")
        buf.write("\u014d\7K\2\2\u014d\u014e\7P\2\2\u014e\u014f\7P\2\2\u014f")
        buf.write("\u0150\7G\2\2\u0150\u0151\7T\2\2\u0151\60\3\2\2\2\u0152")
        buf.write("\u0153\7K\2\2\u0153\u0154\7P\2\2\u0154\u0155\7V\2\2\u0155")
        buf.write("\u0156\7Q\2\2\u0156\62\3\2\2\2\u0157\u0158\7K\2\2\u0158")
        buf.write("\u0159\7U\2\2\u0159\64\3\2\2\2\u015a\u015b\7L\2\2\u015b")
        buf.write("\u015c\7Q\2\2\u015c\u015d\7K\2\2\u015d\u015e\7P\2\2\u015e")
        buf.write("\66\3\2\2\2\u015f\u0160\7N\2\2\u0160\u0161\7G\2\2\u0161")
        buf.write("\u0162\7H\2\2\u0162\u0163\7V\2\2\u01638\3\2\2\2\u0164")
        buf.write("\u0165\7N\2\2\u0165\u0166\7K\2\2\u0166\u0167\7M\2\2\u0167")
        buf.write("\u0168\7G\2\2\u0168:\3\2\2\2\u0169\u016a\7N\2\2\u016a")
        buf.write("\u016b\7K\2\2\u016b\u016c\7O\2\2\u016c\u016d\7K\2\2\u016d")
        buf.write("\u016e\7V\2\2\u016e<\3\2\2\2\u016f\u0170\7P\2\2\u0170")
        buf.write("\u0171\7Q\2\2\u0171\u0172\7V\2\2\u0172>\3\2\2\2\u0173")
        buf.write("\u0174\7P\2\2\u0174\u0175\7W\2\2\u0175\u0176\7N\2\2\u0176")
        buf.write("\u0177\7N\2\2\u0177@\3\2\2\2\u0178\u0179\7Q\2\2\u0179")
        buf.write("\u017a\7P\2\2\u017aB\3\2\2\2\u017b\u017c\7Q\2\2\u017c")
        buf.write("\u017d\7T\2\2\u017dD\3\2\2\2\u017e\u017f\7Q\2\2\u017f")
        buf.write("\u0180\7T\2\2\u0180\u0181\7F\2\2\u0181\u0182\7G\2\2\u0182")
        buf.write("\u0183\7T\2\2\u0183F\3\2\2\2\u0184\u0185\7Q\2\2\u0185")
        buf.write("\u0186\7W\2\2\u0186\u0187\7V\2\2\u0187\u0188\7G\2\2\u0188")
        buf.write("\u0189\7T\2\2\u0189H\3\2\2\2\u018a\u018b\7T\2\2\u018b")
        buf.write("\u018c\7G\2\2\u018c\u018d\7I\2\2\u018d\u018e\7G\2\2\u018e")
        buf.write("\u018f\7Z\2\2\u018f\u0190\7R\2\2\u0190J\3\2\2\2\u0191")
        buf.write("\u0192\7T\2\2\u0192\u0193\7K\2\2\u0193\u0194\7I\2\2\u0194")
        buf.write("\u0195\7J\2\2\u0195\u0196\7V\2\2\u0196L\3\2\2\2\u0197")
        buf.write("\u0198\7T\2\2\u0198\u0199\7N\2\2\u0199\u019a\7K\2\2\u019a")
        buf.write("\u019b\7M\2\2\u019b\u019c\7G\2\2\u019cN\3\2\2\2\u019d")
        buf.write("\u019e\7U\2\2\u019e\u019f\7G\2\2\u019f\u01a0\7N\2\2\u01a0")
        buf.write("\u01a1\7G\2\2\u01a1\u01a2\7E\2\2\u01a2\u01a3\7V\2\2\u01a3")
        buf.write("P\3\2\2\2\u01a4\u01a5\7V\2\2\u01a5\u01a6\7J\2\2\u01a6")
        buf.write("\u01a7\7G\2\2\u01a7\u01a8\7P\2\2\u01a8R\3\2\2\2\u01a9")
        buf.write("\u01aa\7V\2\2\u01aa\u01ab\7T\2\2\u01ab\u01ac\7W\2\2\u01ac")
        buf.write("\u01ad\7G\2\2\u01adT\3\2\2\2\u01ae\u01af\7W\2\2\u01af")
        buf.write("\u01b0\7P\2\2\u01b0\u01b1\7K\2\2\u01b1\u01b2\7Q\2\2\u01b2")
        buf.write("\u01b3\7P\2\2\u01b3V\3\2\2\2\u01b4\u01b5\7W\2\2\u01b5")
        buf.write("\u01b6\7U\2\2\u01b6\u01b7\7K\2\2\u01b7\u01b8\7P\2\2\u01b8")
        buf.write("\u01b9\7I\2\2\u01b9X\3\2\2\2\u01ba\u01bb\7X\2\2\u01bb")
        buf.write("\u01bc\7C\2\2\u01bc\u01bd\7N\2\2\u01bd\u01be\7W\2\2\u01be")
        buf.write("\u01bf\7G\2\2\u01bf\u01c0\7U\2\2\u01c0Z\3\2\2\2\u01c1")
        buf.write("\u01c2\7Y\2\2\u01c2\u01c3\7J\2\2\u01c3\u01c4\7G\2\2\u01c4")
        buf.write("\u01c5\7P\2\2\u01c5\\\3\2\2\2\u01c6\u01c7\7Y\2\2\u01c7")
        buf.write("\u01c8\7J\2\2\u01c8\u01c9\7G\2\2\u01c9\u01ca\7T\2\2\u01ca")
        buf.write("\u01cb\7G\2\2\u01cb^\3\2\2\2\u01cc\u01cd\7C\2\2\u01cd")
        buf.write("\u01ce\7P\2\2\u01ce\u01cf\7[\2\2\u01cf`\3\2\2\2\u01d0")
        buf.write("\u01d1\7G\2\2\u01d1\u01d2\7P\2\2\u01d2\u01d3\7F\2\2\u01d3")
        buf.write("b\3\2\2\2\u01d4\u01d5\7Q\2\2\u01d5\u01d6\7H\2\2\u01d6")
        buf.write("\u01d7\7H\2\2\u01d7\u01d8\7U\2\2\u01d8\u01d9\7G\2\2\u01d9")
        buf.write("\u01da\7V\2\2\u01dad\3\2\2\2\u01db\u01dc\7U\2\2\u01dc")
        buf.write("\u01dd\7Q\2\2\u01dd\u01de\7O\2\2\u01de\u01df\7G\2\2\u01df")
        buf.write("f\3\2\2\2\u01e0\u01e1\7W\2\2\u01e1\u01e2\7P\2\2\u01e2")
        buf.write("\u01e3\7M\2\2\u01e3\u01e4\7P\2\2\u01e4\u01e5\7Q\2\2\u01e5")
        buf.write("\u01e6\7Y\2\2\u01e6\u01e7\7P\2\2\u01e7h\3\2\2\2\u01e8")
        buf.write("\u01e9\7,\2\2\u01e9j\3\2\2\2\u01ea\u01eb\7\61\2\2\u01eb")
        buf.write("l\3\2\2\2\u01ec\u01ed\7\'\2\2\u01edn\3\2\2\2\u01ee\u01ef")
        buf.write("\7-\2\2\u01efp\3\2\2\2\u01f0\u01f1\7/\2\2\u01f1\u01f2")
        buf.write("\7/\2\2\u01f2r\3\2\2\2\u01f3\u01f4\7/\2\2\u01f4t\3\2\2")
        buf.write("\2\u01f5\u01f6\7F\2\2\u01f6\u01f7\7K\2\2\u01f7\u01f8\7")
        buf.write("X\2\2\u01f8v\3\2\2\2\u01f9\u01fa\7O\2\2\u01fa\u01fb\7")
        buf.write("Q\2\2\u01fb\u01fc\7F\2\2\u01fcx\3\2\2\2\u01fd\u01fe\7")
        buf.write("?\2\2\u01fez\3\2\2\2\u01ff\u0200\7@\2\2\u0200|\3\2\2\2")
        buf.write("\u0201\u0202\7>\2\2\u0202~\3\2\2\2\u0203\u0204\7#\2\2")
        buf.write("\u0204\u0080\3\2\2\2\u0205\u0206\7\u0080\2\2\u0206\u0082")
        buf.write("\3\2\2\2\u0207\u0208\7~\2\2\u0208\u0084\3\2\2\2\u0209")
        buf.write("\u020a\7(\2\2\u020a\u0086\3\2\2\2\u020b\u020c\7`\2\2\u020c")
        buf.write("\u0088\3\2\2\2\u020d\u020e\7\60\2\2\u020e\u008a\3\2\2")
        buf.write("\2\u020f\u0210\7*\2\2\u0210\u008c\3\2\2\2\u0211\u0212")
        buf.write("\7+\2\2\u0212\u008e\3\2\2\2\u0213\u0214\7.\2\2\u0214\u0090")
        buf.write("\3\2\2\2\u0215\u0218\5\u009fP\2\u0216\u0218\5\u00a1Q\2")
        buf.write("\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218\u0092\3")
        buf.write("\2\2\2\u0219\u021b\5\u00a5S\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("\u021c\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021d\u0094\3\2\2\2\u021e\u0220\5\u00a5S\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0224\3\2\2\2\u0223\u021f\3\2\2\2")
        buf.write("\u0223\u0224\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0227\7")
        buf.write("\60\2\2\u0226\u0228\5\u00a5S\2\u0227\u0226\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2")
        buf.write("\u022a\u0096\3\2\2\2\u022b\u022c\7^\2\2\u022c\u022d\7")
        buf.write("P\2\2\u022d\u0098\3\2\2\2\u022e\u022f\7\60\2\2\u022f\u0230")
        buf.write("\5\u009dO\2\u0230\u009a\3\2\2\2\u0231\u0232\5\u009dO\2")
        buf.write("\u0232\u009c\3\2\2\2\u0233\u0235\t\4\2\2\u0234\u0233\3")
        buf.write("\2\2\2\u0235\u0238\3\2\2\2\u0236\u0237\3\2\2\2\u0236\u0234")
        buf.write("\3\2\2\2\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0239")
        buf.write("\u023b\t\5\2\2\u023a\u0239\3\2\2\2\u023b\u023c\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u0241\3")
        buf.write("\2\2\2\u023e\u0240\t\4\2\2\u023f\u023e\3\2\2\2\u0240\u0243")
        buf.write("\3\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242")
        buf.write("\u009e\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u024c\7$\2\2")
        buf.write("\u0245\u0246\7^\2\2\u0246\u024b\13\2\2\2\u0247\u0248\7")
        buf.write("$\2\2\u0248\u024b\7$\2\2\u0249\u024b\n\6\2\2\u024a\u0245")
        buf.write("\3\2\2\2\u024a\u0247\3\2\2\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2")
        buf.write("\u024d\u024f\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0250\7")
        buf.write("$\2\2\u0250\u00a0\3\2\2\2\u0251\u0259\7)\2\2\u0252\u0253")
        buf.write("\7^\2\2\u0253\u0258\13\2\2\2\u0254\u0255\7)\2\2\u0255")
        buf.write("\u0258\7)\2\2\u0256\u0258\n\7\2\2\u0257\u0252\3\2\2\2")
        buf.write("\u0257\u0254\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u025b\3")
        buf.write("\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025c")
        buf.write("\3\2\2\2\u025b\u0259\3\2\2\2\u025c\u025d\7)\2\2\u025d")
        buf.write("\u00a2\3\2\2\2\u025e\u0266\7b\2\2\u025f\u0260\7^\2\2\u0260")
        buf.write("\u0265\13\2\2\2\u0261\u0262\7b\2\2\u0262\u0265\7b\2\2")
        buf.write("\u0263\u0265\n\b\2\2\u0264\u025f\3\2\2\2\u0264\u0261\3")
        buf.write("\2\2\2\u0264\u0263\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0269\3\2\2\2\u0268")
        buf.write("\u0266\3\2\2\2\u0269\u026a\7b\2\2\u026a\u00a4\3\2\2\2")
        buf.write("\u026b\u026c\t\t\2\2\u026c\u00a6\3\2\2\2\u026d\u026e\13")
        buf.write("\2\2\2\u026e\u026f\3\2\2\2\u026f\u0270\bT\4\2\u0270\u00a8")
        buf.write("\3\2\2\2\33\2\u00ac\u00b7\u00c4\u00d0\u00d5\u00d9\u00dd")
        buf.write("\u00e3\u00e7\u00e9\u0217\u021c\u0221\u0223\u0229\u0236")
        buf.write("\u023c\u0241\u024a\u024c\u0257\u0259\u0264\u0266\5\2\3")
        buf.write("\2\2\4\2\2\5\2")
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
    WITH = 10
    BY = 11
    CASE = 12
    CROSS = 13
    DESC = 14
    DISTINCT = 15
    ELSE = 16
    EXISTS = 17
    FALSE = 18
    FROM = 19
    GROUP = 20
    HAVING = 21
    IN = 22
    INNER = 23
    INTO = 24
    IS = 25
    JOIN = 26
    LEFT = 27
    LIKE = 28
    LIMIT = 29
    NOT = 30
    NULL_LITERAL = 31
    ON = 32
    OR = 33
    ORDER = 34
    OUTER = 35
    REGEXP = 36
    RIGHT = 37
    RLIKE = 38
    SELECT = 39
    THEN = 40
    TRUE = 41
    UNION = 42
    USING = 43
    VALUES = 44
    WHEN = 45
    WHERE = 46
    ANY = 47
    END = 48
    OFFSET = 49
    SOME = 50
    UNKNOWN = 51
    STAR = 52
    DIVIDE = 53
    MODULE = 54
    PLUS = 55
    MINUSMINUS = 56
    MINUS = 57
    DIV = 58
    MOD = 59
    EQUAL_SYMBOL = 60
    GREATER_SYMBOL = 61
    LESS_SYMBOL = 62
    EXCLAMATION_SYMBOL = 63
    BIT_NOT_OP = 64
    BIT_OR_OP = 65
    BIT_AND_OP = 66
    BIT_XOR_OP = 67
    DOT = 68
    LR_BRACKET = 69
    RR_BRACKET = 70
    COMMA = 71
    STRING_LITERAL = 72
    DECIMAL_LITERAL = 73
    REAL_LITERAL = 74
    NULL_SPEC_LITERAL = 75
    DOT_ID = 76
    ID = 77
    ERROR_RECONGNIGION = 78

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN", u"MYSQLCOMMENT", 
                                                          u"ERRORCHANNEL" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ALL'", "'AND'", "'AS'", "'ASC'", "'BETWEEN'", "'WITH'", "'BY'", 
            "'CASE'", "'CROSS'", "'DESC'", "'DISTINCT'", "'ELSE'", "'EXISTS'", 
            "'FALSE'", "'FROM'", "'GROUP'", "'HAVING'", "'IN'", "'INNER'", 
            "'INTO'", "'IS'", "'JOIN'", "'LEFT'", "'LIKE'", "'LIMIT'", "'NOT'", 
            "'NULL'", "'ON'", "'OR'", "'ORDER'", "'OUTER'", "'REGEXP'", 
            "'RIGHT'", "'RLIKE'", "'SELECT'", "'THEN'", "'TRUE'", "'UNION'", 
            "'USING'", "'VALUES'", "'WHEN'", "'WHERE'", "'ANY'", "'END'", 
            "'OFFSET'", "'SOME'", "'UNKNOWN'", "'*'", "'/'", "'%'", "'+'", 
            "'--'", "'-'", "'DIV'", "'MOD'", "'='", "'>'", "'<'", "'!'", 
            "'~'", "'|'", "'&'", "'^'", "'.'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "SPEC_MYSQL_COMMENT", "COMMENT_INPUT", "LINE_COMMENT", 
            "ALL", "AND", "AS", "ASC", "BETWEEN", "WITH", "BY", "CASE", 
            "CROSS", "DESC", "DISTINCT", "ELSE", "EXISTS", "FALSE", "FROM", 
            "GROUP", "HAVING", "IN", "INNER", "INTO", "IS", "JOIN", "LEFT", 
            "LIKE", "LIMIT", "NOT", "NULL_LITERAL", "ON", "OR", "ORDER", 
            "OUTER", "REGEXP", "RIGHT", "RLIKE", "SELECT", "THEN", "TRUE", 
            "UNION", "USING", "VALUES", "WHEN", "WHERE", "ANY", "END", "OFFSET", 
            "SOME", "UNKNOWN", "STAR", "DIVIDE", "MODULE", "PLUS", "MINUSMINUS", 
            "MINUS", "DIV", "MOD", "EQUAL_SYMBOL", "GREATER_SYMBOL", "LESS_SYMBOL", 
            "EXCLAMATION_SYMBOL", "BIT_NOT_OP", "BIT_OR_OP", "BIT_AND_OP", 
            "BIT_XOR_OP", "DOT", "LR_BRACKET", "RR_BRACKET", "COMMA", "STRING_LITERAL", 
            "DECIMAL_LITERAL", "REAL_LITERAL", "NULL_SPEC_LITERAL", "DOT_ID", 
            "ID", "ERROR_RECONGNIGION" ]

    ruleNames = [ "SPACE", "SPEC_MYSQL_COMMENT", "COMMENT_INPUT", "LINE_COMMENT", 
                  "ALL", "AND", "AS", "ASC", "BETWEEN", "WITH", "BY", "CASE", 
                  "CROSS", "DESC", "DISTINCT", "ELSE", "EXISTS", "FALSE", 
                  "FROM", "GROUP", "HAVING", "IN", "INNER", "INTO", "IS", 
                  "JOIN", "LEFT", "LIKE", "LIMIT", "NOT", "NULL_LITERAL", 
                  "ON", "OR", "ORDER", "OUTER", "REGEXP", "RIGHT", "RLIKE", 
                  "SELECT", "THEN", "TRUE", "UNION", "USING", "VALUES", 
                  "WHEN", "WHERE", "ANY", "END", "OFFSET", "SOME", "UNKNOWN", 
                  "STAR", "DIVIDE", "MODULE", "PLUS", "MINUSMINUS", "MINUS", 
                  "DIV", "MOD", "EQUAL_SYMBOL", "GREATER_SYMBOL", "LESS_SYMBOL", 
                  "EXCLAMATION_SYMBOL", "BIT_NOT_OP", "BIT_OR_OP", "BIT_AND_OP", 
                  "BIT_XOR_OP", "DOT", "LR_BRACKET", "RR_BRACKET", "COMMA", 
                  "STRING_LITERAL", "DECIMAL_LITERAL", "REAL_LITERAL", "NULL_SPEC_LITERAL", 
                  "DOT_ID", "ID", "ID_LITERAL", "DQUOTA_STRING", "SQUOTA_STRING", 
                  "BQUOTA_STRING", "DEC_DIGIT", "ERROR_RECONGNIGION" ]

    grammarFileName = "MySqlLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


