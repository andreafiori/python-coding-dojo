import unittest
from src.python_algorithms.algorithms.math.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(Calculator.add(1, 3), 4)

    def test_subtract(self):
        subtract = Calculator.subtract(4, 3)
        self.assertEqual(subtract, 1)

    def test_divide(self):
        divided = Calculator.divide(12, 3)
        self.assertEqual(divided, 4)

    def test_divide_by_zero_exception(self):
        with self.assertRaises(Exception):
            Calculator.divide(4, 0)
