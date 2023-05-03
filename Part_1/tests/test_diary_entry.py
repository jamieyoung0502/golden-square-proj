from lib.Diary_entry import *

def test_word_count():
    diary_entry = DiaryEntry ("26th April", "Wrote some tests for classes")
    result = diary_entry.count_words()
    assert result == 5

def test_format():
    diary_entry = DiaryEntry ("26th April", "Wrote some tests for classes")
    result = diary_entry.format()
    assert result == "26th April: Wrote some tests for classes"

def test_reading_time():
    diary_entry = DiaryEntry ("26th April", "Wrote some tests for classes")
    result = diary_entry.reading_time(1)
    assert result == 5

def test_reading_chunk():
    diary_entry = DiaryEntry ("26th April", "Wrote some tests for classes")
    result = diary_entry.reading_chunk(1, 4)
    assert result == "Wrote some tests for"

