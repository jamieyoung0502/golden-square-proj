class Track:
    def __init__(self, title, artist):
        # title and artist are both strings
        self.artist = artist
        self.title = title
        

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        return keyword in self.artist or keyword in self.title