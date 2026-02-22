import unittest
from src.python_algorithms.algorithms.math.prime_factors import PrimeFactors


class PrimeFactorsTest(unittest.TestCase):
    def test_get_prime_numbers(self):
        self.assertEqual(PrimeFactors.get_prime_numbers(8), [2, 2, 2])

    def test_is_prime_is_true(self):
        self.assertTrue( PrimeFactors.is_prime(11) )

    def test_is_prime_is_false(self):
        self.assertFalse( PrimeFactors.is_prime(10) )