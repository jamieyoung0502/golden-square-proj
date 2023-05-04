# Multi-Class Planned Design Recipe
# 1. Describe the Problem
"""
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

"""
"""
As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.
"""

"""
As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.
"""

# Use the twilio-python package to implement this next one. You will need to use mocks too.

"""As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.
"""
# 2. Design the Class System
# Design the interfaces of each of your classes and how they will work together to achieve the job of the program. You can use diagrams to visualise the relationships between classes.

"""
> view menu with list of dishes and prices (dish class feeding in to menu class)

> need to be able to select a number of several available dishes (My Order class?)

> view itemised receipt with a grand total (method in dish selector for this?)

> after order placed send a text using (twilio-python api?) to say the food will arrive by (+45 mins seems reasonable)


"""









# Steps 3, 4, and 5 then operate as a cycle.

# 3. Create Examples as Integration Tests
# Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.













# 4. Create Examples as Unit Tests
# Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.


"testing the Menu class"

def test_add_single_mock_dish_to_menu_view_menu():
    dish1 = Mock()
    menu = Menu()
    dish1.format_dish.return_value = "cheese Pizza: 8.50"
    menu.add_dish_to_menu(dish1)
    assert menu.view_menu() == ["cheese Pizza: 8.50"]

def test_add_mulitple_mock_dishes_to_menu_view_menu():
    menu = Menu()
    dish1 = Mock()
    dish1.format_dish.return_value = "cheese Pizza: 8.50"
    dish2 = Mock()
    dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
    dish3 =  Mock()
    dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.add_dish_to_menu(dish3)
    assert menu.view_menu() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00"
    ]

def test_remove_dishes_from_menu():
    menu = Menu()
    dish1 = Mock()
    dish1.format_dish.return_value = "cheese Pizza: 8.50"
    dish2 = Mock()
    dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
    dish3 =  Mock()
    dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.add_dish_to_menu(dish3)
    assert menu.view_menu() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00"
    ]
    menu.remove_dish_from_menu(dish3)
    assert menu.view_menu() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50"

    ]

"testing place order class"

def test_add_single_mock_dish_to_my_order_view_order():
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
    dish1.price = 8.50
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    assert my_order.view_my_order() == [
        "cheese Pizza: 8.50",
        "TOTAL = 8.50"
        
        ]

def test_add_mulitple_mock_dishes_to_my_order_view_order():
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
    dish1.price = 8.50
    dish2 = Mock()
    dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
    dish2.price = 9.50
    dish3 = Mock()
    dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
    dish3.price = 11.00
    dish3 =  Dish ("Ham and Pineapple Pizza", 11.00)
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    my_order.add_to_order(dish2)
    my_order.add_to_order(dish3)
    assert my_order.view_my_order() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00",
    "TOTAL = 29.00"

    ]

def test_remove_from_order():
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
    dish1.price = 8.50
    dish2 = Mock()
    dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
    dish2.price = 9.50
    dish3 = Mock()
    dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
    dish3.price = 11.00
    dish3 =  Dish ("Ham and Pineapple Pizza", 11.00)
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    my_order.add_to_order(dish2)
    my_order.add_to_order(dish3)
    assert my_order.view_my_order() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00",
    "TOTAL = 29.00"
    ]
    my_order.remove_from_order(dish3)
    assert my_order.view_my_order() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "TOTAL = 18.00"
    ]

def test_clear_order():
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
    dish1.price = 8.50
    dish2 = Mock()
    dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
    dish2.price = 9.50
    dish3 = Mock()
    dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
    dish3.price = 11.00
    dish3 =  Dish ("Ham and Pineapple Pizza", 11.00)
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    my_order.add_to_order(dish2)
    my_order.add_to_order(dish3)
    assert my_order.view_my_order() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00",
    "TOTAL = 29.00"
    ]
    my_order.clear_order()
    assert my_order.view_my_order() == ["Total = 0"]

def test_place_order_sends_message():
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
    dish1.price = 8.50
    dish2 = Mock()
    dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
    dish2.price = 9.50
    dish3 = Mock()
    dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
    dish3.price = 11.00
    dish3 =  Dish ("Ham and Pineapple Pizza", 11.00)
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    my_order.add_to_order(dish2)
    my_order.add_to_order(dish3)
    assert my_order.view_my_order() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00",
    "TOTAL = 29.00"
    ]
    assert my_order.place_order() == "Your order has been placed" #add a text message gets sent - unsure how to confirm this at the moment!






# 5. Implement the Behaviour
# For each example you create as a test, implement the behaviour that allows the class to behave according to your example.








# Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.

