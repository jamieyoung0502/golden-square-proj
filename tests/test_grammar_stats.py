from lib.grammar_stats import *

def test_percentage_good_4_True_2_False():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello, This string is correct.")
    grammar_stats.check("Hello, This string is correct.")
    grammar_stats.check("Hello, This string is correct.")
    grammar_stats.check("Hello, This string is correct.")
    grammar_stats.check("hello, This string is not correct.")
    grammar_stats.check("Hello, This string is not correct")
    result = grammar_stats.percentage_good()
    assert result == 66


