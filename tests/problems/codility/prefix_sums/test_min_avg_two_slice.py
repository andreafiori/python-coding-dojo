import unittest
import random

from src.python_algorithms.problems.codility.prefix_sums.min_avg_two_slice import MinAvgTwoSlice

class MinAvgTwoSliceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.min_avg_two_slice = MinAvgTwoSlice()

    def test_example(self):
        self.assertEqual(self.min_avg_two_slice.solution([4, 2, 2, 5, 1, 5, 8]), 1)
        self.assertEqual(self.min_avg_two_slice.solution([5, 2, 2, 100, 1, 1, 100]), 4)
        self.assertEqual(self.min_avg_two_slice.solution([11, 2, 10, 1, 100, 2, 9, 2, 100]), 1)

    def test_three(self):
        # self.assertEqual(self.min_avg_two_slice.solution([-3, -5, -8, -4, -10]), 2)
        # self.assertEqual(self.min_avg_two_slice.solution([-8, -6, -10]), 0)
        self.assertEqual(self.min_avg_two_slice.solution([1, -1, 1, -1]), 1)

    def test_random(self):
        A = [random.randint(*self.min_avg_two_slice.RANGE_N) for _ in range(2, 10)]
        print(A)
        print(self.min_avg_two_slice.solution(A))

    # def test_large_ones(self):
        # Numbers from -1 to 1, N = ~100000
        # how to test?

    # TypeError: can't multiply sequence by non-int of type 'float'
    # def test_extreme(self):
    #     A = [self.min_avg_two_slice.RANGE_N[1]] * (self.min_avg_two_slice.RANGE_A[1] / 3) + [self.min_avg_two_slice.RANGE_N[0]] * (self.min_avg_two_slice.RANGE_A[1] / 3)
    #     idx = self.min_avg_two_slice.solution(A)
    #     print(idx, A[idx-3:idx+3])