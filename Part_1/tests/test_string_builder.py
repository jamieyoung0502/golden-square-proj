from lib.string_builder import *

def test_size_and_output_single_input():
    string_builder = StringBuilder()
    string_builder.add('word')
    result = string_builder.size()
    result2 = string_builder.output()
    assert result == 4
    assert result2 == 'word'

def test_size_and_output_double_input():
    string_builder = StringBuilder()
    string_builder.add('word')
    string_builder.add('second')
    result = string_builder.size()
    result2 = string_builder.output()
    assert result == 10
    assert result2 == 'wordsecond'

def test_sentence():
    string_builder = StringBuilder()
    string_builder.add('This')
    string_builder.add(' is')
    string_builder.add(' a')
    string_builder.add(' complete')
    string_builder.add(' sentence!')
    result = string_builder.size()
    result2 = string_builder.output()
    assert result == 28
    assert result2 == 'This is a complete sentence!'