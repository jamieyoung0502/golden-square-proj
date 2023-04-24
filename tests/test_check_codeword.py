from lib.check_codeword import *

def test_check_correct():
    assert check_codeword('horse') == "Correct! Come in."

def test_check_close():
    assert check_codeword("house") == "Close, but nope."

def test_check_wrong():
    assert check_codeword("fjhdsfj") ==  "WRONG!"
