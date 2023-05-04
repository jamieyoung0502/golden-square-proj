from lib.Music_library import *
from lib.track import *


"""When a track is added self.track_list contains that track"""

def test_track_added_to_library():
    music_library = MusicLibrary()
    track_1 = Track ("Bloodshot", "Enter Shikari")
    music_library.add(track_1)
    assert music_library.track_list == [track_1]

def test_multiple_tracks_added_to_library():
    music_library = MusicLibrary()
    track_1 = Track ("Bloodshot", "Enter Shikari")
    track_2 = Track ("Old Fashioned", "Frightented Rabbit")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.track_list == [track_1, track_2]

def test_search_function_with_whole_word():
    music_library = MusicLibrary()
    track_1 = Track ("Bloodshot", "Enter Shikari")
    track_2 = Track ("Old Fashioned", "Frightented Rabbit")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("Old") == [track_2]

def test_search_function_with_part_of_word():
    music_library = MusicLibrary()
    track_1 = Track ("Bloodshot", "Enter Shikari")
    track_2 = Track ("Old Fashioned", "Frightented Rabbit")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search("kari") == [track_1]


