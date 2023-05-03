class Diary():
    def __init__(self):
        self.entries = []
        self.task_list = None       

    def add(self, entry):
        self.entries.append(entry)

    def view_all(self):
        return self.entries

    def reading_time(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        highest_count = 0
        longest_so_far = None
        for item in self.entries:
            if item.word_count() <= words_user_can_read and item.word_count() > highest_count:
                longest_so_far = item.contents
                highest_count = item.word_count()
        return longest_so_far
    
    def create_task_list(self, all_tasks):
        self.task_list = all_tasks
    
    def view_completed_tasks(self):
        task_display = []
        for item in self.task_list.tasks:
            if item.complete == True:
                task_display.append(item.task)
        return task_display

    def view_incomplete_tasks(self):
        task_display = []
        for item in self.task_list.tasks:
            if item.complete == False:
                task_display.append(item.task)
        return task_display
    
    def list_contact_numbers(self):
        # search diary entries for 11 digit numbers
        # display list of numbers from entries
        phone_numbers = []
        for entry in self.entries:
            for word in entry.contents.split():
                if word.isdigit() and len(word) == 11:
                    phone_numbers.append(word)
        return phone_numbers
