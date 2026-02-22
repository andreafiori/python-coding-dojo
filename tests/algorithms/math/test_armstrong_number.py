import unittest

from src.python_algorithms.algorithms.math.armstrong_number import ArmstrongNumber

class TestArmstrongNumber(unittest.TestCase):
    def setUp(self):
        self.armstrong = ArmstrongNumber()

    def test_is_armstrong_number_single_digits(self):
        """Test single-digit Armstrong numbers (0-9)."""
        for i in range(10):
            self.assertTrue(self.armstrong.is_armstrong_number(i), f"{i} should be Armstrong")

    def test_is_armstrong_number_three_digits(self):
        """Test known 3-digit Armstrong numbers."""
        armstrong_nums = [153, 370, 371, 407]
        for num in armstrong_nums:
            self.assertTrue(self.armstrong.is_armstrong_number(num), f"{num} should be Armstrong")

    def test_is_armstrong_number_four_digits(self):
        """Test known 4-digit Armstrong numbers."""
        self.assertTrue(self.armstrong.is_armstrong_number(1634))

    def test_is_armstrong_number_not_armstrong(self):
        """Test non-Armstrong numbers."""
        non_armstrong = [10, 100, 123, 200]
        for num in non_armstrong:
            self.assertFalse(self.armstrong.is_armstrong_number(num), f"{num} should not be Armstrong")

    def test_is_armstrong_number_zero(self):
        """Test zero as Armstrong number."""
        self.assertTrue(self.armstrong.is_armstrong_number(0))

    def test_is_armstrong_number_three_digits_specific(self):
        """Test the 3-digit specific method with known cases."""
        self.assertTrue(self.armstrong.is_armstrong_number_three_digits(153))
        self.assertTrue(self.armstrong.is_armstrong_number_three_digits(371))
        self.assertFalse(self.armstrong.is_armstrong_number_three_digits(100))
