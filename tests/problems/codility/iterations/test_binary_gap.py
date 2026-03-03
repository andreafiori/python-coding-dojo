import unittest

from python_algorithms.problems.codility.iterations.binary_gap import BinaryGap

class TestBinaryGap(unittest.TestCase):

    def setup_class(self):
        self.binaryGap = BinaryGap()

    def test_example1(self):
        self.assertEqual(5, self.binaryGap.solution(1041))

    def test_example2(self):
        self.assertEqual(0, self.binaryGap.solution(15))

    def test_extremes(self):
        self.assertEqual(0, self.binaryGap.solution(1))
        self.assertEqual(1, self.binaryGap.solution(5))
        self.assertEqual(0, self.binaryGap.solution(self.binaryGap.MAXINT))

    def test_trailing_zeros(self):
        self.assertEqual(self.binaryGap.solution(6), 0)
        self.assertEqual(self.binaryGap.solution(328), 2)

    def test_simple1(self):
        self.assertEqual(self.binaryGap.solution(9), 2)
        self.assertEqual(self.binaryGap.solution(11), 1)

    def test_simple2(self):
        self.assertEqual(self.binaryGap.solution(19), 2)
        self.assertEqual(self.binaryGap.solution(42), 1)

    def test_simple3(self):
        self.assertEqual(self.binaryGap.solution(1162), 3)
        self.assertEqual(self.binaryGap.solution(5), 1)

    def test_medium1(self):
        self.assertEqual(self.binaryGap.solution(51712), 2)
        self.assertEqual(self.binaryGap.solution(20), 1)

    def test_medium2(self):
        self.assertEqual(self.binaryGap.solution(561892), 3)
        self.assertEqual(self.binaryGap.solution(9), 2)

    def test_medium3(self):
        self.assertEqual(self.binaryGap.solution(66561), 9)

    def test_large1(self):
        self.assertEqual(self.binaryGap.solution(6291457), 20)

    def test_large2(self):
        self.assertEqual(self.binaryGap.solution(74901729), 4)

    def test_large3(self):
        self.assertEqual(self.binaryGap.solution(805306369), 27)

    def test_large4(self):
        self.assertEqual(self.binaryGap.solution(1376796946), 5)

    def test_large5(self):
        self.assertEqual(self.binaryGap.solution(1073741825), 29)

    def test_large6(self):
        self.assertEqual(self.binaryGap.solution(1610612737), 28)

    def test_non_int(self):
        self.assertRaises(TypeError, self.binaryGap.solution, 1.0)

    def test_zero(self):
        self.assertRaises(ValueError, self.binaryGap.solution, 0)

    def test_maxint_plus_one(self):
        self.assertRaises(ValueError, self.binaryGap.solution, 2147483648)
