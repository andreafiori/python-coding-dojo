import unittest

from src.python_algorithms.problems.leetcode.ltc_0258_add_digits import AddDigits

class TestAddDigits(unittest.TestCase):
    def test_add_digits(self):
        assert AddDigits().add(38) == 2
