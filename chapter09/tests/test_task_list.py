from lib.Task_List import *
from lib.Task import *

# Initially empty list
def test_initially_empty_task_list():
    task_list = TaskList()
    assert task_list.tasks == []

# After adding one task the list contains one item
def test_add_one_task_to_list():
    task_list = TaskList()
    task_1 = Task("walk the dog")
    task_list.add_task(task_1)
    assert task_list.tasks == [task_1]

# After adding two tasks the list contains two items
def test_add_two_tasks_to_list():
    task_list = TaskList()
    task_1 = Task("walk the dog")
    task_2 = Task("walk the cat")
    task_list.add_task(task_1)
    task_list.add_task(task_2)
    assert task_list.tasks == [task_1, task_2]