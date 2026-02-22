import unittest

from src.python_algorithms.problems.codility.prefix_sums.count_div import solution


class TestCountDiv(unittest.TestCase):
    MAX_INT = int(2e9)
    INT_RANGE = (1, MAX_INT)

    def test_example(self):
        self.assertEqual(solution(6, 11, 2), 3)

    def test_small(self):
        self.assertEqual(solution(5, 11, 2), 3)
        self.assertEqual(solution(6, 12, 2), 4)
        self.assertEqual(solution(5, 12, 2), 4)
        self.assertEqual(solution(5, 13, 2), 4)

    def test_edges(self):
        self.assertEqual(solution(0, 0, 1), 1)
        self.assertEqual(solution(0, 1, 1), 2)
        self.assertEqual(solution(1, 1, 2), 0)
        self.assertEqual(solution(10, 20, 10), 2)
        self.assertEqual(solution(9, 21, 10), 2)

    def test_max_min(self):
        self.assertEqual(solution(0, self.MAX_INT, 1), self.MAX_INT + 1)
