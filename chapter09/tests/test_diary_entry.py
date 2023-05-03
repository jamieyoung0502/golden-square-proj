from lib.Diary_Entry import *

"""
Initially when a diary entry is created
self.title and self.contents update"""

def test_title_and_contents_are_added():
    entry_1 = DiaryEntry("My Title 1", "one two three")
    assert entry_1.title == "My Title 1"
    assert entry_1.contents == "one two three"