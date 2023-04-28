class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents
        

    def format(self):
        return f"{self.title}: {self.contents}"
    

    def count_words(self):
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def reading_chunk(self, wpm, minutes):
        output = ""
        num_words_to_return = wpm * minutes
        words = self.contents.split()
        if output == "":
            output  += " ".join(words[0:num_words_to_return])
            return output
        else:
            word_count = output.split
            output += " ".join(words[word_count:word_count + 4])
            return output


diary_entry = DiaryEntry ("26th April", "Wrote some tests for classes")
print (diary_entry.reading_chunk(1,4))
print (diary_entry.reading_chunk(1,4))     





        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.