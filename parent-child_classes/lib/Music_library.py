class MusicLibrary:

    def __init__(self):
        self.track_list = []

    def add(self, track):
        self.track_list.append(track)

    def search(self, keyword):
        lst = []
        for track in self.track_list:
            if track.matches(keyword) == True:
                lst.append(track)
        return lst
