class Menu():
    
    def __init__(self):
        # self.menu will contain a list of all dish objects - list
        self.menu = []
    

    def add_dish_to_menu(self, dish):
        # adds dish object to self.menu
        self.menu.append(dish)

    def remove_dish_from_menu(self, dish):
        # removes dish object from self.menu
        self.menu.remove(dish)
        

    def view_menu(self):
        # will return a nice readable list of all dish objects for customer to read
        readable_menu = []
        for meal in self.menu:
            readable_menu.append (meal.format_dish())
        return readable_menu
