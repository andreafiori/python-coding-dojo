import pytest

from src.python_algorithms.problems.codility.counting_elements.perm_check import PermCheck

@pytest.fixture
def perm_check():
    return PermCheck()


class TestPermCheck:
    def test_solution_is_zero(self, perm_check):
        v = [1, 1]
        x = [4, 1, 3]
        y = [2]
        z = [2,2]
        assert perm_check.solution(v) == 0
        assert perm_check.solution(x) == 0
        assert perm_check.solution(y) == 0
        assert perm_check.solution(z) == 0

    def test_solution_is_one(self, perm_check):
        x = [4, 1, 3, 2]
        assert perm_check.solution(x) == 1

    def test_bottom_edge_is_zero(self):
        x = []
        assert perm_check.solution(x) == 0

    def test_bottom_edge_is_one(self, perm_check):
        x = [1]
        y = [1, 2]
        z = [2, 1]
        assert perm_check.solution(x) == 1
        assert perm_check.solution(y) == 1
        assert perm_check.solution(z) == 1

# assert self.solution([1, 2, 3]), 1)
# assert self.solution([3, 2, 1]), 1)
# assert self.solution([5, 2, 1]), 0)
# assert self.solution([3, 1]), 0)

# def test_duplicates(self):
#     assert self.solution([3, 3, 3, 3, 2, 1]), 0)

# def test_extreme(self, perm_check):
#     # full complement of math
#     arr = range(1, PermCheck.ARR_RANGE[1] + 1)
#     random.shuffle(arr)
#     assert self.solution(arr), 1)

#     # full complement with one missing
#     arr.remove(random.randint(1,len(arr)))
#     assert self.solution(arr), 0)
