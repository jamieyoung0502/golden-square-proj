import pytest
from lib.present import *

def test_present_wrapping_before_unwrapping():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrapping_present_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message ==  "No contents have been wrapped."  

