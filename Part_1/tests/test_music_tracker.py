from lib.music_tracker import *
import pytest
"""
testing to make sure a blank dictionary is created when initilised. Nothing is added so when view is called we expect a blank dictionary to be output

"""
def test_view_with_nothing_added():
    music_tracker = MusicTracker()
    assert music_tracker.view() == {}

"""
when the user adds a valid artist name as a Key and track name as Value the dictionary is added to
"""
def test_add_valid_new_artist_and_song_title():
    music_tracker = MusicTracker()
    music_tracker.add("Fleetwood Mac", "Don't stop")
    assert music_tracker.view() == {"Fleetwood Mac": ["Don't stop"]}

def test_add_two_valid_new_artists_and_song_titles():
    music_tracker = MusicTracker()
    music_tracker.add("Fleetwood Mac", "Don't stop")
    music_tracker.add("Enter Shikari", "Bloodshot")
    assert music_tracker.view() == {"Fleetwood Mac": ["Don't stop"], "Enter Shikari": ["Bloodshot"]}

def test_add_one_valid_new_artist_and_second_song_title():
    music_tracker = MusicTracker()
    music_tracker.add("Fleetwood Mac", "Don't stop")
    music_tracker.add("Fleetwood Mac", "Songbird")
    assert music_tracker.view() == {"Fleetwood Mac": ["Don't stop","Songbird"]}

def test_add_two_valid_new_artists_one_with_second_song_title():
    music_tracker = MusicTracker()
    music_tracker.add("Fleetwood Mac", "Don't stop")
    music_tracker.add("Enter Shikari", "Bloodshot")
    music_tracker.add("Fleetwood Mac", "Songbird")
    assert music_tracker.view() == {"Fleetwood Mac": ["Don't stop","Songbird"],"Enter Shikari": ["Bloodshot"] }

def test_enter_empty_band_name():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add("", "Don't stop")
    error_message = str(err.value)
    assert error_message == "Band name cannot be blank"

def test_enter_empty_song_name():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add("Enter Shikari", "")
    error_message = str(err.value)
    assert error_message == "Song name cannot be blank"

def test_blank_artist_and_song_names():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        music_tracker.add("", "")
    error_message = str(err.value)
    assert error_message == "Both Band and Song name are blank"




