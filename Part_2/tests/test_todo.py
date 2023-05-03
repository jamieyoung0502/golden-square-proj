from lib.Todo import *

def test_task_is_added():
    to_do = Todo ("Walk the dog")
    assert to_do.task == "Walk the dog"

def test_initial_complete_is_False():
    todo_list = Todo("walk the dog")
    assert todo_list._complete == False
