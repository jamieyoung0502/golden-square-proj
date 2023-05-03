class TaskList():
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)

    def view_all_tasks(self):
        return self.tasks
