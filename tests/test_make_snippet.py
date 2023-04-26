from lib.make_snippet import *

def test_string_with_4words():
    result = make_snippet("These are four words")
    assert result == "These are four words"

def test_string_with_7words():
    result = make_snippet("There are seven words in this sentence")
    assert result == "There are seven words in..."