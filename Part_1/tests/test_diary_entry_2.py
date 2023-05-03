from lib.diary_entry_2 import *

def test_public_properties():
    diary_entry = DiaryEntry ("Day 1", "Today is a Monday")
    assert diary_entry.title == "Day 1"
    assert diary_entry.contents == "Today is a Monday"

def test_count_words():
    diary_entry = DiaryEntry ("Day 1", "Today is a Monday")
    assert diary_entry.count_words() == 4

def test_reading_time():
    diary_entry = DiaryEntry ("Day 1", "Today is a Monday")
    assert diary_entry.reading_time(3) == 2

def test_reading_chunk():
    diary_entry = DiaryEntry ("Day 1", "one two three four five six")
    assert diary_entry.reading_chunk(1, 2) == "one two"
    assert diary_entry.reading_chunk(1, 2) == "three four"
    assert diary_entry.reading_chunk(1, 1) == "five"
    assert diary_entry.reading_chunk(1, 2) == "six"
    assert diary_entry.reading_chunk(3, 1) == "one two three"

