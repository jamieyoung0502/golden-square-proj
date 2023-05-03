from lib.grammar_checker import *
import pytest
"""As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark."""

# def test_caps_at_start_correct():
#    result = grammar_checker("Hello, my name is Jamie")
#    assert result == "Your string starts with a capital letter!"

# def test_caps_at_start_incorrect():
#    result = grammar_checker("hello, my name is Jamie")
#    assert result == "Your string does not start with a capital letter!"

def test_starts_with_caps_and_ends_with_correct_punctuation():
    result = grammar_checker("Hello, my name is Jamie!")
    assert result == "Your string starts with a capital letter and has correct punctuation at the end!"

def test_starts_with_caps_and_ends_with_incorrect_punctuation():
    result = grammar_checker("Hello, my name is Jamie")
    assert result == "Your string starts with a capital letter but has incorrect punctuation at the end!"

def test_does_not_start_with_caps_and_ends_with_correct_punctuation():
    result = grammar_checker("hello, my name is Jamie.")
    assert result == "Your string does not start with a capital letter but has correct punctuation at the end!"

def test_does_not_start_with_caps_and_ends_with_incorrect_punctuation():
    result = grammar_checker("hello, my name is Jamie")
    assert result == "Your string does not start with a capital letter and has incorrect punctuation at the end!"

def test_input_not_a_string():
    with pytest.raises(Exception) as e:
        result = grammar_checker(123)
    error_message = str(e.value)
    assert error_message == "input must be a string!"

def test_input_a_blank_string():
    with pytest.raises(Exception) as e:
        result = grammar_checker("")
    error_message = str(e.value)
    assert error_message == "input cannot be a blank string!"
