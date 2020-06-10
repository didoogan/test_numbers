import pytest

from main import find_numbers


@pytest.fixture
def number_list():
    return [10, 5, 2, 5, 7, 7, 49]


class TestNumbers:

    def test_success(self, number_list):
        result = find_numbers(number_list)
        assert result == [{5, 2}]
