import pytest
from lib.password_checker import *

def test_password_length_over8():
    password_checker = PasswordChecker()
    result = password_checker.check("password123")
    assert result == True

def test_password_length_under8():
    password_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        password_checker.check("qwerty")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters." 

