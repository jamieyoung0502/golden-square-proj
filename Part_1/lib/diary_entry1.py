class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents
        self._read_so_far = 0 
        

    def format(self):
        return f"{self.title}: {self.contents}"
    

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return int(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        #calculate number of words to read
        words_to_read = int(wpm * minutes)

        #check if there are more words to read
        if self._read_so_far >= len(self.contents.split()):
            self._read_so_far = 0
            chunk = " ".join(self.contents.split(" ")[self._read_so_far :self._read_so_far + words_to_read])
            self._read_so_far += words_to_read
            return chunk
        if self._read_so_far < len(self.contents.split()):
            chunk = " ".join(self.contents.split(" ")[self._read_so_far :self._read_so_far + words_to_read])
            self._read_so_far += words_to_read
            return chunk
        

    
entry1 = DiaryEntry ("Today" , "Today is going to be a great day.")
print (entry1.reading_chunk(2,2))
print (entry1.reading_chunk(1,2))
print (entry1.reading_chunk(1,3))
print (entry1.reading_chunk(1,2))
print (entry1.reading_chunk(1,5))