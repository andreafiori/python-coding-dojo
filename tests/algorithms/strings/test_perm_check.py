from src.python_algorithms.problems.codility.counting_elements.perm_check import PermCheck

# example1
# example2
# extreme_min_max = single element with min/max value
# single element
# double = two elements
# antiSum1 = total sum is correct but it is not a permutation, N <= 10
# small_permutation = permutation + one element occurs twice, N = ~100
# medium_permutation = permutation + few elements occur twice, N = ~10000
# antisum2 = total sum is correct but it is not a permutation, N = ~100000
# large_permutation: permutation + one element occurs twice, N = ~100000
# large_range: sequence 1,2,...,N  N=~100000
# extreme_values: all the same values, N=~100000

class TestPermCheck:

    def test_solution_is_zero(self):
        v = [1, 1]
        x = [4, 1, 3]
        y = [2]
        z = [2,2]
        assert PermCheck.solution(v) == 0
        assert PermCheck.solution(x) == 0
        assert PermCheck.solution(y) == 0
        assert PermCheck.solution(z) == 0

    def test_solution_is_one(self):
        x = [4, 1, 3, 2]
        assert PermCheck.solution(x) == 1

    def test_bottom_edge_is_zero(self):
        x = []
        assert PermCheck.solution(x) == 0

    def test_bottom_edge_is_one(self):
        x = [1]
        y = [1, 2]
        z = [2, 1]
        assert PermCheck.solution(x) == 1
        assert PermCheck.solution(y) == 1
        assert PermCheck.solution(z) == 1

# self.assertEqual(self.solution([1, 2, 3]), 1)
# self.assertEqual(self.solution([3, 2, 1]), 1)
# self.assertEqual(self.solution([5, 2, 1]), 0)
# self.assertEqual(self.solution([3, 1]), 0)

# def test_duplicates(self):
#     self.assertEqual(self.solution([3, 3, 3, 3, 2, 1]), 0)

# def test_extreme(self):
#     # full complement of math
#     arr = range(1, PermCheck.ARR_RANGE[1] + 1)
#     random.shuffle(arr)
#     self.assertEqual(self.solution(arr), 1)

#     # full complement with one missing
#     arr.remove(random.randint(1,len(arr)))
#     self.assertEqual(self.solution(arr), 0)
