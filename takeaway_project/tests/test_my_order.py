from lib.MyOrder import MyOrder
from unittest.mock import Mock

def test_add_single_mock_dish_to_my_order_view_order():
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
    dish1.price = 8.50
    my_order = MyOrder()
    my_order.add_to_order(dish1)
    assert my_order.view_my_order() == [
        "Cheese Pizza: 8.50",
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


# def test_place_order_sends_message():
#     dish1 = Mock()
#     dish1.format_dish.return_value = "Cheese Pizza: 8.50"
#     dish1.price = 8.50
#     dish2 = Mock()
#     dish2.format_dish.return_value = "Vegtable Pizza: 9.50"
#     dish2.price = 9.50
#     dish3 = Mock()
#     dish3.format_dish.return_value = "Ham and Pineapple Pizza: 11.00"
#     dish3.price = 11.00
#     dish3 =  Dish ("Ham and Pineapple Pizza", 11.00)
#     my_order = MyOrder()
#     my_order.add_to_order(dish1)
#     my_order.add_to_order(dish2)
#     my_order.add_to_order(dish3)
#     assert my_order.view_my_order() == [
#     "Cheese Pizza: 8.50",
#     "Vegtable Pizza: 9.50",
#     "Ham and Pineapple Pizza: 11.00",
#     "TOTAL = 29.00"
#     ]
#     assert my_order.place_order() == "Your order has been placed" #add a text message gets sent - unsure how to confirm this at the moment!
