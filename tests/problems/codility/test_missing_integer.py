
import unittest
import random

from src.python_algorithms.problems.codility.counting_elements.missing_integer import MissingInteger

class TestMissingInteger(unittest.TestCase):
    def setup_class(self):
        self.missing_integer = MissingInteger()

    def test_example(self):
        self.assertEqual(self.missing_integer.solution([1, 3, 6, 4, 1, 2]), 5)

    def test_extreme_single(self):
        self.assertEqual(self.missing_integer.solution([2]), 1)
        self.assertEqual(self.missing_integer.solution([1]), 2)
        self.assertEqual(self.missing_integer.solution([-1]), 1)

    def test_simple(self):
        self.assertEqual(self.missing_integer.solution([2,3,4,6,10,1000]), 1)
        self.assertEqual(self.missing_integer.solution([-1, 0, 1, 2, 3, 4, 5, 6, 10, 1000]), 7)
        self.assertEqual(self.missing_integer.solution([1000, -1, 10, 3, -5, 2, 11, 59, 1]), 4)

    def test_extreme_min_max_int(self):
        self.assertEqual(1, self.missing_integer.solution([MissingInteger.ELEMENT_RANGE[0], MissingInteger.ELEMENT_RANGE[1], -10]))

    # def test_positive_only(self):
    #     arr = range(1, 101) + range(102, 201)
    #     random.shuffle(arr)
    #     self.assertEqual(self.missing_integer.solution(arr), 101)

    # def test_negative_only(self):
    #     arr = range(-100, 0)
    #     random.shuffle(arr)
    #     self.assertEqual(self.missing_integer.solution(arr), 1)

    def test_no_gaps(self):
        self.assertEqual(self.missing_integer.solution([1, 2, 3, 4, 5]), 6)

    def test_duplicates(self):
        self.assertEqual(self.missing_integer.solution([1, 1, 1, 3, 3, 3]), 2)

    # def test_large_2(self):
    #     # create big array of ints
    #     arr = range(1,100000)
    #     random.shuffle(arr)
    #     # remove one
    #     missing_idx = random.randint(1, len(arr))
    #     missing_int = arr[missing_idx]
    #     del arr[missing_idx]
    #     # run it
    #     self.assertEqual(self.missing_integer.solution(arr), missing_int)

    def test_monster_positive(self):
        arr = [random.randint(*MissingInteger.ELEMENT_RANGE) for _ in range(1, MissingInteger.N_RANGE[1])]
        random.shuffle(arr)
        """ print self.missing_integer.solution(arr), arr """
