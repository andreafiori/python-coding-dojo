import unittest
from src.python_algorithms.algorithms.math.factorial import Factorial


class LeapYearsTest(unittest.TestCase):
    def test_factorial_w_num_greater_than_1(self):
        self.assertTrue(Factorial.calculate(3), 9)

    def test_factorial_w_one(self):
        self.assertTrue(Factorial.calculate(1), 1)
