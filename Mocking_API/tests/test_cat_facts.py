from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_get_cat_fact_returns_fact():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact": "A cat fact"}
    cat_fact = CatFacts(requester_mock)
    assert cat_fact.provide() == "Cat fact: A cat fact"