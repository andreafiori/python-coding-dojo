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
    #     self.assertEqual(solution([0, 1, 2, 3, 4]), 5)

    # def test_edges(self):
    #     self.assertEqual(solution([]), 0)
    #     self.assertEqual(solution([0]), 1)
    #     self.assertEqual(solution([1]), 1)
    #     self.assertEqual(solution([0, 1]), 2)
    #     self.assertEqual(solution([-1, 1]), 2)
    #     self.assertEqual(solution([RANGE_A[0], RANGE_A[1]]), 2)

    # def test_medium(self):
    #     self.assertEqual(solution([1] * 500), 1)
    #     self.assertEqual(solution([x for x in range(-250, 250)]), 500)
    #     self.assertEqual(solution([x for x in range(-500, 500, 2)]), 500)
    #     self.assertEqual(solution([x for x in range(-500, 500, 2)] * 2), 500)

    # def test_random(self):
    #     A = [random.randint(*RANGE_A) for _ in range(*RANGE_N)]
    #     """ print solution(A), A """

    # def test_extreme(self):
    #     A = [x for x in range(*RANGE_N)]
    #     self.assertEqual(solution(A), RANGE_N[1])
