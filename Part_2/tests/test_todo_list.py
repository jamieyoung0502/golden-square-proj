from lib.Todo_list import *

def test_initial_list_is_empty():
    todo_list = TodoList()
    assert todo_list.todos == []
