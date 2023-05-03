from lib.diary import *
from lib.diary_entry_2 import *

def test_add_diary_entry_to_diary_then_run_all():
    diary = Diary()
    diary_entry1 = DiaryEntry("day 1", "Today is a Monday")
    diary_entry2 = DiaryEntry("day 2", "Today is a Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.all() == [diary_entry1, diary_entry2]


def test_count_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("day 1", "Today is a Monday")
    diary_entry2 = DiaryEntry("day 2", "Today is Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.count_words() == 7

def test_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("day 1", "Today is a Monday")
    diary_entry2 = DiaryEntry("day 2", "Today is Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.reading_time(2) == 4

def test_find_best_entry_perfect_match():
    diary = Diary()
    diary_entry1 = DiaryEntry("day 1", "Today is a Monday")
    diary_entry2 = DiaryEntry("day 2", "Today is Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(1,4) == "Today is a Monday"

def test_find_best_entry_not_perfect_match():
    diary = Diary()
    diary_entry1 = DiaryEntry("day 1", "Today is Monday")
    diary_entry2 = DiaryEntry("day 2", "Today is probably a Tuesday")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2,2) == "Today is Monday"

