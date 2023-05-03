from lib.count_words import *

def test_count_9words():
    result = count_words("Hi, my name is Rachel. I'm from Northern Ireland.")
    assert result == "This string has 9 words."

def test_count_1words():
    result = count_words("Hello")
    assert result == "This string has 1 word." 

def test_count_0words():
    result = count_words("")
    assert result == "You need to enter at least one word."   