import unittest

from src.python_algorithms.algorithms.recursion.fibonacci import Fibonacci

class FibonacciTest(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_calculate(self):
        self.assertEqual( self.fibonacci.calculate(9), 21)
