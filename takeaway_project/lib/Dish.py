class Dish():

    def __init__(self, name, price):
        # dish name - string
        # dish price - string
        if type(price) != str:
            raise Exception("Price must be input as string")
        self.name = name
        self.price = price
        

    def format_dish(self):
        # format object to display "dish name: price"
        return f"{self.name}: {self.price}"
        
