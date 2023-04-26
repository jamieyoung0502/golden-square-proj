#As a user
#So that I can keep track of my tasks
#I want to check if a text includes the string #TODO.

from lib.task_tracker import *
import pytest

def test_todo_caps_in_text():
    result = task_tracker("#TODO: go to the shop")
    assert result == True

def test_todo_lowercase_in_text():
    result = task_tracker("#todo: go to the shop")
    assert result == True

def test_input_not_string():
    with pytest.raises(Exception) as e:
        result = task_tracker(123)
    error_message = str(e.value)
    assert error_message == "Input type must be a string."

def test_blank_string():
    with pytest.raises(Exception) as e:
        result = task_tracker("")
    error_message = str(e.value)
    assert error_message == "This string must have some contents."

def test_todo_placement():
    result = task_tracker("on my #ToDo list: go to the shop") 
    assert result == True              