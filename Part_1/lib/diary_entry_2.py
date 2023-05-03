import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self._read_so_far = 0 
        

    def count_words(self):
        words = self.contents.split(" ")
        return len(words)

    def reading_time(self, wpm):
        return math.ceil (self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self.contents.split(" ")
        if self._read_so_far >= len(words):
            self._read_so_far = 0
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start: chunk_end]
        self._read_so_far = chunk_end
        return " ".join(chunk_words)

