import unittest
from src.online.leetcode.add_digits import add_digits

class TestAddDigits(unittest.TestCase):
    def test_add_digits(self):
        self.assertEqual(add_digits(38), 2)
