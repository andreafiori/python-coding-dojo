import unittest
import random
from src.python_algorithms.problems.codility.arrays.cyclic_rotation import cyclic_rotation


class TestCyclicRotation(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(cyclic_rotation([6, 3, 8, 9, 7], 0), [6, 3, 8, 9, 7])

    def test_one(self):
        self.assertEqual(cyclic_rotation([6, 3, 8, 9, 7], 1), [7, 6, 3, 8, 9])

    def test_example1(self):
        self.assertEqual(cyclic_rotation([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_full(self):
        self.assertEqual(cyclic_rotation([6, 3, 8, 9, 7], 5), [6, 3, 8, 9, 7])

    def test_empty(self):
        self.assertEqual(cyclic_rotation([], 5), [])

    def test_random(self):
        ARRAY_RANGE = (-1000, 1000)
        INT_RANGE = (0, 100)
        N = random.randint(*INT_RANGE)
        K = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
        """ 
        print N, K, A
        print solution(A, K)
        """
