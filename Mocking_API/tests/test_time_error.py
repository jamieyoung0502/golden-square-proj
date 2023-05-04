from unittest.mock import Mock
from lib.time_error import TimeError


def test_requester_works():
    requester_mock = Mock(name="requester")
    response_mock = Mock(name="response")
    time_mock = Mock(name="time")

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 3}
    time_mock.time.return_value = 2

    time_error = TimeError(requester_mock, time_mock)
    assert time_error.error() == 1
