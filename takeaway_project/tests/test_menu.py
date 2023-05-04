from lib.Menu import Menu
from unittest.mock import Mock


def test_add_single_mock_dish_to_menu_view_menu():
    dish1 = Mock()
    menu = Menu()
    dish1.format_dish.return_value = "cheese Pizza: 8.50"
    menu.add_dish_to_menu(dish1)
    assert menu.view_menu() == ["cheese Pizza: 8.50"]

def test_add_mulitple_mock_dishes_to_menu_view_menu():
    menu = Menu()
    dish1 = Mock()
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
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
    dish1.format_dish.return_value = "Cheese Pizza: 8.50"
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