from lib.gratitudes import *

def test_adding_1gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("health")
    result = gratitudes.format()
    assert result == "Be grateful for: health"

def test_adding_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("health")
    gratitudes.add("family")
    result = gratitudes.format()
    assert result == "Be grateful for: health, family"