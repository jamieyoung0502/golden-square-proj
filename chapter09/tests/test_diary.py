from lib.Diary import *


"""
Initially when Diary is made self.entries will be a blank list
"""

def test_initially_entries_blank():
    diary = Diary()
    assert diary.entries == []
