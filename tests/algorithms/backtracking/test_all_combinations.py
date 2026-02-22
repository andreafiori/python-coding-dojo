import pytest

from src.python_algorithms.algorithms.backtracking.all_combinations import BacktrackingAllCombinations

@pytest.fixture
def backtracker():
    """Provide a fresh BacktrackingAllCombinations instance for each test."""
    return BacktrackingAllCombinations()

class TestBacktrackingAllCombinations:
    """Test suite for BacktrackingAllCombinations class."""

    def test_combination_lists_with_itertools(self, backtracker):
        """Test itertools implementation matches expected combinations."""
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        result = backtracker.combination_lists(n=4, k=2)
        assert result == expected

    def test_combination_lists_edge_cases(self, backtracker):
        """Test edge cases for itertools implementation."""
        assert backtracker.combination_lists(n=1, k=0) == [[]]
        assert backtracker.combination_lists(n=1, k=1) == [[1]]
        assert backtracker.combination_lists(n=3, k=3) == [[1, 2, 3]]

    @pytest.mark.parametrize("n,k,expected", [
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (5, 4, [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]),
        (3, 1, [[1], [2], [3]]),
        (1, 0, [[]]),
        (1, 1, [[1]]),
        (0, 0, [[]]),
    ])
    def test_generate_all_combinations_happy_path(self, backtracker, n, k, expected):
        """Test backtracking generates correct combinations for valid inputs."""
        result = backtracker.generate_all_combinations(n, k)
        assert result == expected

    def test_generate_all_combinations_equivalence(self, backtracker):
        """Verify backtracking matches itertools for n=1 to 5, k=1 to 5."""
        from itertools import combinations
        expected_func = lambda n, k: [list(x) for x in combinations(range(1, n + 1), k)]

        for n in range(1, 6):
            for k in range(1, n + 1):  # k <= n
                backtrack_result = backtracker.generate_all_combinations(n, k)
                itertools_result = expected_func(n, k)
                assert backtrack_result == itertools_result, f"Mismatch at n={n}, k={k}"

    def test_generate_all_combinations_negative_k(self, backtracker):
        """Test ValueError raised for negative k."""
        with pytest.raises(ValueError, match="k must not be negative"):
            backtracker.generate_all_combinations(n=10, k=-1)

    def test_generate_all_combinations_negative_n(self, backtracker):
        """Test ValueError raised for negative n."""
        with pytest.raises(ValueError, match="n must not be negative"):
            backtracker.generate_all_combinations(n=-1, k=10)

    def test_create_all_state_complete(self, backtracker):
        """Test create_all_state builds full combinations."""
        result = []
        backtracker.create_all_state(1, 4, 2, [], result)
        expected = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
        assert result == expected

    @pytest.mark.parametrize("start,total,level,current,expected", [
        (1, 3, 3, [], [[1, 2, 3]]),  # Full combination
        (2, 2, 1, [1], [[1, 2]]),    # Partial continuation
        (1, 0, 0, [], [[]]),         # Zero level (empty)
        (1, 4, 0, [1, 2], [[1, 2]]), # Zero level with existing
        (5, 4, 2, [1, 2], []),       # Invalid range (no results)
    ])
    def test_create_all_state_edge_cases(self, backtracker, start, total, level, current, expected):
        """Test create_all_state edge cases from docstring."""
        result = []
        backtracker.create_all_state(start, total, level, current[:], result)  # Copy current
        assert result == expected

    # def test_lists_are_immutable(self, backtracker):
    #     """Verify combinations lists don't share references."""
    #     result = backtracker.generate_all_combinations(3, 2)
    #     # Modify one list - others should remain unchanged
    #     result[0].append(99)
    #     assert result[1] == [2, 3], "Modifying one combination shouldn't affect others"
