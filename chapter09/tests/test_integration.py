from lib.Diary import *
from lib.Diary_Entry import *
from lib.Task import *
from lib.Task_List import *
'''
When I add a diary entry to Diary
It gets added to the dictionary
'''
def test_add_one_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    diary.add(entry_1)
    assert diary.view_all() == [entry_1]

'''
When I add two diary entries
There are two items in the dictionary
'''
def test_add_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    entry_2 = DiaryEntry("My Title 2", "four five six")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.view_all() == [entry_1, entry_2]

def test_reading_time_for_one_readable_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    diary.add(entry_1)
    assert diary.reading_time(1,3) == "one two three"

def test_reading_time_for_two_readable_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    entry_2 = DiaryEntry("My Title 2", "five six seven")
    diary.add(entry_2)
    diary.add(entry_1)
    assert diary.reading_time(3,1) == "five six seven"

def test_reading_time_returns_longest_of_two_readable_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three four")
    entry_2 = DiaryEntry("My Title 2", "five six seven")
    diary.add(entry_2)
    diary.add(entry_1)
    assert diary.reading_time(5,1) == "one two three four"

def test_reading_time_empty_list():
    diary = Diary()
    assert diary.reading_time(5,1) == None

def test_reading_time_entries_all_too_long():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three four")
    entry_2 = DiaryEntry("My Title 2", "five six seven")
    diary.add(entry_2)
    diary.add(entry_1)
    assert diary.reading_time(2,1) == None

def test_add_multiple_tasks_to_diary():
    diary = Diary()
    task_1 = Task("walk the dog")
    task_2 = Task("walk the ferret")
    task_list = TaskList()
    task_list.add_task(task_1)
    task_list.add_task(task_2)
    diary.create_task_list(task_list)
    assert diary.view_incomplete_tasks() == ["walk the dog", "walk the ferret"]

def test_view_completed_tasks():
    diary = Diary()
    task_1 = Task("walk the dog")
    task_2 = Task("walk the ferret")
    task_list = TaskList()
    task_list.add_task(task_1)
    task_list.add_task(task_2)
    diary.create_task_list(task_list)
    assert diary.view_incomplete_tasks() == ["walk the dog", "walk the ferret"]
    task_1.mark_complete()
    assert diary.view_completed_tasks() == ["walk the dog"]
    assert diary.view_incomplete_tasks() == ["walk the ferret"] 

def test_list_contact_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "12345678901")
    entry_2 = DiaryEntry("My Title 2", "12345678902")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.list_contact_numbers() == ["12345678901", "12345678902"]