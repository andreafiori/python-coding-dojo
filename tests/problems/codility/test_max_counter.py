import unittest
import random

from src.python_algorithms.problems.codility.counting_elements.max_counters import MaxCounters

"""
example
extreme_small: all max_counter operations
single: only one counter
small_random1: small random test 6 max_counter operations
small_random2: small random test, 10 max_counter operations
medium_random1: medium random test, 50 max_counter operations
medium_random2: medium random test, 500 max_counter operations
large_random1: large random test, 2120 max_counter operations
large_random2: large random test, 10000 max_counter operations
extreme_large: all max_counter operations
"""
class TestMaxCounter(unittest.TestCase):

    def setup_class(self):
        self.maxCounters = MaxCounters()

    def test_example(self):
        self.assertEqual(self.maxCounters.solution(5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])

    def test_singles(self):
        self.assertEqual(self.maxCounters.solution(1, [1]), [1])
        self.assertEqual(self.maxCounters.solution(1, [1, 2]), [1])
        self.assertNotEqual(self.maxCounters.solution(1, [1,2,2]), [2])
        self.assertEqual(self.maxCounters.solution(1, [1, 1, 2, 1, 1]), [4])

    def test_doubles(self):
        self.assertEqual(self.maxCounters.solution(2, [1, 1, 1, 2]), [3, 1])
        self.assertEqual(self.maxCounters.solution(2, [1, 1, 1, 3]), [3, 3])
        self.assertEqual(self.maxCounters.solution(2, [3, 1, 1, 1]), [3, 0])
        self.assertEqual(self.maxCounters.solution(2, [3, 1, 1, 2]), [2, 1])
        self.assertEqual(self.maxCounters.solution(2, [1, 2, 3, 1, 2]), [2, 2])
        self.assertEqual(self.maxCounters.solution(2, [1, 1, 3, 1, 1]), [4, 2])
        self.assertEqual(self.maxCounters.solution(2, [1, 1, 3, 2, 2]), [2, 4])

    def test_extreme(self):
        # ten thousand counters, 90 thousand operations
        arr = [random.randint(1, 9999) for _ in range(90000)]
        """ print self.maxCounters.solution(9999, arr) """
