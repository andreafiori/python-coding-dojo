import unittest

from src.python_algorithms.algorithms.math.leap_years import is_leap

class LeapYearsTest(unittest.TestCase):
    def test_is_leap(self):
        self.assertTrue( is_leap(2000) )

    def test_is_leap_return_false(self):
        self.assertFalse( is_leap(2001) )
