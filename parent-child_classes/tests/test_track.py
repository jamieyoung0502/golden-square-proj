from lib.track import *

def test_artist_and_title_saved_correctly():
    track = Track("Bloodshot", "Enter Shikari")
    assert track.artist == "Enter Shikari"
    assert track.title == "Bloodshot"

def test_matches_method_functions():
    track = Track("Bloodshot", "Enter Shikari")
    assert track.matches ("Bloodshot") == True
    assert track.matches ("Enter Shikari") == True
    assert track.matches ("bloodshot") == False
    assert track.matches ("anything else") == False