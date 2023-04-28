from lib.to_do_list import *
import pytest


"""Given a single item added to the list
calling view list will return that item
"""

def test_view_list_for_single_valid_item():
    to_do_list = To_do_list()
    to_do_list.add_to_list("walk the dog")
    assert to_do_list.view_list() == "Your list: walk the dog"

def test_view_list_for_multiple_valid_items():
    to_do_list = To_do_list()
    to_do_list.add_to_list("walk the dog")
    to_do_list.add_to_list("Do the dishes")
    to_do_list.add_to_list("pay bills")
    assert to_do_list.view_list() == "Your list: walk the dog, Do the dishes, pay bills"

def test_add_to_list_non_string_item():
    to_do_list = To_do_list()
    with pytest.raises(Exception) as err:
        to_do_list.add_to_list(123)
    error_message = str(err.value)
    assert error_message == "Input must be a non blank string"

def test_add_to_list_blank_string_item():
    to_do_list = To_do_list()
    with pytest.raises(Exception) as err:
        to_do_list.add_to_list("")
    error_message = str(err.value)
    assert error_message == "Input must be a non blank string"

def test_remove_from_list_valid():
    to_do_list = To_do_list()
    to_do_list.add_to_list("walk the dog")
    to_do_list.add_to_list("Do the dishes")
    to_do_list.add_to_list("pay bills")
    to_do_list.remove_from_list("walk the dog")
    assert to_do_list.view_list() == "Your list: Do the dishes, pay bills"


