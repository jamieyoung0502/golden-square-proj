class DiaryEntry():
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format_entry(self, title, contents):
        # format the entry into "My Title: My contents" 
        pass

    def word_count(self):
        return len(self.contents.split())
        