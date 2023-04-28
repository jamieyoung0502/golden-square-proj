# As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.

class To_do_list():

    def __init__(self):
        # each new instance will get a blank list to add tasks to.
        self.item_list = []


    def add_to_list(self,task):
        # using add_to_list will add a task input by the user to the item list. The task input should be a string otherwise an exception is raised
        if type(task) != str or task == "":
            raise Exception ("Input must be a non blank string")
        self.item_list.append(task)
        return self.item_list
    
    def view_list(self):
        # When view_list is called the user will get a nice view of the item list.
        list = ", ".join(self.item_list)
        return f"Your list: {list}"
        

    def remove_from_list(self, task):
        # given a task already on the list calling this will remove that item from the list
        if task in self.item_list:
            self.item_list.remove(task)
        return self.item_list
