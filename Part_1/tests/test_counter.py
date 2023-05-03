from lib.counter import *

def test_add_5():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_add_negative_10():
    counter = Counter()
    counter.add(-10)
    result = counter.report()
    assert result == "Counted to -10 so far."   

def test_add_0():
    counter = Counter()
    counter.add(0)
    result = counter.report()
    assert result == "Counted to 0 so far."    