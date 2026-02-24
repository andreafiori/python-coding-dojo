import unittest

from src.python_algorithms.problems.leetcode.ltc_0258_add_digits import add_digits

class TestAddDigits(unittest.TestCase):
    def test_add_digits(self):
        self.assertEqual(add_digits(38), 2)
