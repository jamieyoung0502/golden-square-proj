from lib.Music_library import *
from unittest.mock import Mock

def test_initially_blank_track_list():
    music_library = MusicLibrary()
    assert music_library.track_list == []

def test_searching_function_with_whole_word():
    music_library = MusicLibrary()

    Fake_matching = Mock()
    Fake_matching.matches.return_value = True
    Fake_not_matching = Mock()
    Fake_not_matching.matches.return_value = False
    music_library.add(Fake_matching)
    music_library.add(Fake_not_matching)
    assert music_library.search("Ol") == [Fake_matching]