class TodoList:
    def __init__(self):
        self.todos = []
        self.completed = []
        self._incomplete = []


    def add(self, todo):
        self.todos.append(todo)
    
    def incomplete(self):
        for task in self.todos:
            if task._complete == False:
                self._incomplete.append(task)
        return self._incomplete



    def complete(self):
        for task in self.todos:
            if task._complete == True:
                self.completed.append(task)
        return self.completed
        

    def give_up(self):
        for task in self.todos:
            if task._complete == False:
                task.mark_complete()
