import pytest

from python_algorithms.algorithms.backtracking.combination_sum import CombinationSum

class TestCombinationSum:
    """
    The fixture creates a fresh CombinationSum instance per test for isolation.
    Results are compared after sorting by length then elements to handle order variations from backtracking. All tests pass based on the class docstring examples.
    """
    @pytest.fixture
    def solver(self):
        return CombinationSum()

    @pytest.mark.parametrize(
        "candidates, target, expected",
        [
            ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
            ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ],
    )

    def test_combination_sum_valid_inputs(self, solver, candidates, target, expected):
        result = solver.combination_sum(candidates, target)
        assert sorted(result, key=lambda x: (len(x), x)) == sorted(expected, key=lambda x: (len(x), x))

    def test_empty_candidates_raises_value_error(self, solver):
        with pytest.raises(ValueError, match="Candidates list should not be empty"):
            solver.combination_sum([], 1)

    def test_negative_candidates_raises_value_error(self, solver):
        with pytest.raises(ValueError, match="All elements in candidates must be non-negative"):
            solver.combination_sum([-8, 2.3, 0], 1)
