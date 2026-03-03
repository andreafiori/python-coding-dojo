import unittest
from python_algorithms.algorithms.math.numbers_util import NumbersUtil


class NumbersUtilTest(unittest.TestCase):
    def test_is_palindrome_as_true(self):
        self.assertTrue(NumbersUtil.is_palindrome(121))

    def test_is_palindrome_as_false(self):
        self.assertFalse(NumbersUtil.is_palindrome(567))

    def test_check_convert_base_two(self):
        self.assertEqual(NumbersUtil.convert(25, 2), '11001')

    def test_check_convert_base_hex(self):
        self.assertEqual(NumbersUtil.convert(25, 16), '19')

    def test_is_prime_to_be_true(self):
        self.assertTrue(NumbersUtil.is_prime(11))

    def test_is_prime_to_be_false(self):
        self.assertFalse(NumbersUtil.is_prime(12))

    def test_find_smallest_divisor(self):
        self.assertEqual(NumbersUtil.smallest_divisor(75), 3)

    def test_is_armstrong_number_to_be_true(self):
        self.assertTrue(NumbersUtil.is_armstrong_number(407))
 
    def test_is_armstrong_number_to_be_false(self):
        self.assertFalse(NumbersUtil.is_armstrong_number(663))
