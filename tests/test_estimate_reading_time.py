from lib.reading_time import *
import pytest

"""As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute."""

def test_reading_time_200_words():
    book = " ".join(["word" for i in range (0, 200)])
    assert reading_time(book) == 1 

def test_reading_time_800_words():
    text = " ".join(["word" for i in range (0, 800)])
    assert reading_time(text) == 4

def test_reading_time_100_words():
    text = " ".join(["word" for i in range (0, 100)])
    assert reading_time(text) == 0.5

def test_reading_time_blank_string():
    text = ""
    with pytest.raises(Exception) as e:
        reading_time(text)
    error_message = str(e.value)
    assert error_message == "You cannot input a blank string"

def test_reading_input_not_a_string():
    text = 12
    with pytest.raises(Exception) as e:
        reading_time(text)
    error_message = str(e.value)
    assert error_message == "input is not a string"