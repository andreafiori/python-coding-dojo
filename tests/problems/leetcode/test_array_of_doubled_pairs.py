import unittest

from src.python_algorithms.problems.leetcode.array_of_doubled_pairs import ArrayOfDoubledPairs


class ArrayOfDoubledPairsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s = ArrayOfDoubledPairs()

    def test_can_reorder_doubled_false_case1(self):
        self.assertFalse(self.s.can_reorder_doubled([3, 1, 3, 6]))

    def test_can_reorder_doubled_false_case2(self):
        self.assertFalse(self.s.can_reorder_doubled([2, 1, 2, 6]))

    def test_can_reorder_doubled_false_case3(self):
        self.assertFalse(self.s.can_reorder_doubled([1, 2, 4, 16, 8, 4]))

    def test_can_reorder_doubled_true_case(self):
        self.assertTrue(self.s.can_reorder_doubled([4, -2, 2, -4]))
