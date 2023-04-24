from lib.greet import *

def test_greeting():
    result = greet('Jamie')

    assert result == "Hellohg, Jamie!"