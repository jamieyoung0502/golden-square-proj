"""As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them."""

class MusicTracker():

    def __init__(self):
        # when a new instance is created a blank dictionary will be added
        self.music_list = {}

    def add(self, artist, song):
# key = sting (artist name)
# value = list (song names)
# the add method will add the artist as a key to the dictionary and track name as a value. If a key already the value will be appended
        
        if artist.strip() == "" and song.strip() == "":
            raise Exception ("Both Band and Song name are blank")
        if artist.strip() == "":
            raise Exception ("Band name cannot be blank")
        if song.strip() == "":
            raise Exception ("Song name cannot be blank")
        
        if artist not in self.music_list:
            self.music_list[artist] = []
        self.music_list[artist].append(song)


    def view(self):
        # when called with display a nicely formatted list of the music tracker contents.
        return self.music_list
    

