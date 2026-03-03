import pytest

from python_algorithms.problems.leetcode.ltc_0258_add_digits import AddDigits

@pytest.fixture
def add_digits():
    return AddDigits()

class TestAddDigits:
    def test_add_digits(self, add_digits):
        assert add_digits.add(38) == 2
