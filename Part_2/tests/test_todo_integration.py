from lib.Todo import *
from lib.Todo_list import *

# test add works with instances of todo class
def test_add_todo_list_integration():
    to_do_list = TodoList()
    to_do_1 = Todo("Walk the dog")
    to_do_list.add(to_do_1)
    assert to_do_list.incomplete() == [to_do_1]

def test_complete_and_incomplete_lists_populating():
    to_do_list = TodoList()
    to_do_1 = Todo("Walk the dog")
    to_do_2 = Todo("Feed the cat")
    to_do_3 = Todo("Groom the hamster")
    to_do_list.add(to_do_1)
    to_do_list.add(to_do_2)
    to_do_list.add(to_do_3)
    Todo.mark_complete(to_do_1)
    Todo.mark_complete(to_do_3)
    assert to_do_list.incomplete() == [to_do_2]
    assert to_do_list.complete() == [to_do_1, to_do_3]
    
def test_give_up_add_all_to_complete_list():
    to_do_list = TodoList()
    to_do_1 = Todo("Walk the dog")
    to_do_2 = Todo("Feed the cat")
    to_do_3 = Todo("Groom the hamster")
    to_do_list.add(to_do_1)
    to_do_list.add(to_do_2)
    to_do_list.add(to_do_3)
    Todo.mark_complete(to_do_1)
    to_do_list.give_up()
    assert to_do_list.incomplete() == []
    assert to_do_list.complete() == [to_do_1, to_do_2, to_do_3]

