from lib.Dish import Dish
from lib.Menu import Menu
from lib.MyOrder import MyOrder


def test_add_single_dish_to_menu_view_menu():
    dish1 = Dish("Cheese Pizza", "8.50")
    menu = Menu()
    menu.add_dish_to_menu(dish1)
    assert menu.view_menu() == ["Cheese Pizza: 8.50"]

def test_add_mulitple_dishes_to_menu_view_menu():
    dish1 = Dish("Cheese Pizza", "8.50")
    dish2 = Dish("Vegtable Pizza", "9.50")
    dish3 =  Dish ("Ham and Pineapple Pizza", "11.00")
    menu = Menu()
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.add_dish_to_menu(dish3)
    assert menu.view_menu() == [
    "Cheese Pizza: 8.50",
    "Vegtable Pizza: 9.50",
    "Ham and Pineapple Pizza: 11.00"
    ]

def test_remove_dishes_from_menu():
    dish1 = Dish("Cheese Pizza", "8.50")
    dish2 = Dish("Vegtable Pizza", "9.50")
    dish3 =  Dish ("Ham and Pineapple Pizza", "11.00")
    menu = Menu()
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
    "Vegtable Pizza: 9.50",
    ]

def test_add_single_dish_to_my_order_view_order():
    dish1 = Dish("Cheese Pizza", "8.50")
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    assert my_order.view_my_order() == [
        "Cheese Pizza: 8.50",
        "TOTAL = 8.50"
        ]
    
def test_add_mulitple_dishes_to_my_order_view_order():
    dish1 = Dish("Cheese Pizza", "8.50")
    dish2 = Dish("Vegtable Pizza", "9.50")
    dish3 =  Dish ("Ham and Pineapple Pizza", "11.00")
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
    dish1 = Dish("Cheese Pizza", "8.50")
    dish2 = Dish("Vegtable Pizza", "9.50")
    dish3 =  Dish ("Ham and Pineapple Pizza", "11.00")
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
    dish1 = Dish("Cheese Pizza", "8.50")
    dish2 = Dish("Vegtable Pizza", "9.50")
    dish3 =  Dish ("Ham and Pineapple Pizza", "11.00")
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
    assert my_order.view_my_order() == ["TOTAL = 0.00"]

"""Everything below this point will be testing the TWILIO phone messages
I will be coming back to this after everything else is written"""

def test_place_order_sends_message():
    dish1 = Dish("Cheese Pizza", "8.50")
    dish2 = Dish("Vegtable Pizza", "9.50")
    dish3 =  Dish ("Ham and Pineapple Pizza", "11.00")
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


