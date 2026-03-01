import pytest

from src.python_algorithms.problems.codility.sorting.distinct import Distinct

@pytest.fixture
def distinct_instance():
    """Provide a fresh Distinct instance for each test."""
    return Distinct()

class TestDistinct:
    def test_solution_is_three(self, distinct_instance):
        x = [2, 1, 1, 2, 3, 1]
        assert distinct_instance.solution(x) == 3

    # def test_simple(self):
    #     assert (solution([0, 1, 2, 3, 4]), 5

    # def test_edges(self):
    #     assert solution([]) == 0
    #     assert solution([0]) == 1
    #     assert solution([1]) == 1
    #     assert solution([0, 1]) == 2
    #     assert solution([-1, 1]) == 2
    #     assert solution([RANGE_A[0], RANGE_A[1]]) == 2

    # def test_medium(self):
    #     assert solution([1] * 500) == 1
    #     assert solution([x for x in range(-250, 250)]) == 500
    #     assert solution([x for x in range(-500, 500, 2)]) == 500
    #     assert solution([x for x in range(-500, 500, 2)] * 2) == 500

    # def test_random(self):
    #     A = [random.randint(*RANGE_A) for _ in range(*RANGE_N)]

    # def test_extreme(self):
    #     A = [x for x in range(*RANGE_N)]
    #     assert (solution(A), RANGE_N[1])
