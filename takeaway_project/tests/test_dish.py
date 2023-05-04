from lib.Dish import Dish
import pytest

def test_dish_name_and_price_attributes():
    dish1 = Dish("Meat Feast Pizza", "14.00")
    assert dish1.name == "Meat Feast Pizza"
    assert dish1.price == "14.00"

def test_price_input_as_string():
    with pytest.raises(Exception) as e:
        dish1 = Dish("Meat Feast Pizza", 14.00)
    error_message = str(e.value)
    assert error_message == "Price must be input as string"

def test_format_dish():
    dish1 = Dish("Meat Feast Pizza", "14.00")
    assert dish1.format_dish() == "Meat Feast Pizza: 14.00"
    



