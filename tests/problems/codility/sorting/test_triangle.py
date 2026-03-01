
import unittest

class TestExercise(unittest.TestCase):
    def test_example(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), 1)
        self.assertEqual(solution([10, 50, 5, 1]), 0)

    def test_lowballs(self):
        self.assertEqual(0, solution([]))
        self.assertEqual(0, solution([0]))
        self.assertEqual(0, solution([0, 1]))

    def test_simple(self):
        A = [5, 3, 3]
        self.assertEqual(1, solution(A))

    def test_large_negative(self):
        self.assertEqual(0, solution([-1] * RANGE_N[1]))

if __name__ == '__main__':
    unittest.main()


"""
example - positive answer
example1 - zero answer
extreme_empty - empty sequence
extreme_single - 1 element sequence
extreme_two_elems - 2 element sequence
extreme_negative1 - three equal negative math
extreme_arith_overflow1 - overflow test, 3 maxints
extreme_arith_overflow2 - overflow test, 10 and 2 minints
extreme_arith_overflow3 - overflow test, 0 and 2 maxints
medium1 - chaotic sequence of values [0..100K] length 30
medium2 - chaotic sequence of values [0..1K] length 50
medium3 - chaotic sequence of values [0..1K] length 100
large1 - chaotic sequence of values [0..100K] length 10K
large2 - 1 followed by ascending sequence ~50K elements [0..100K] length ~50K
large_random - chaotic sequence [0..1M] length 100K
large_negative - chaotic sequence of negative values [-1M..-1] length 100K
large_negative2 - chaotic sequence of negative values [-10..-1], length 100K
large_negative3 - sequence of -1 values, length 100K
"""
