import pytest

from src.python_algorithms.problems.codility.prefix_sums.count_div import CountDiv

@pytest.fixture
def count_div():
    return CountDiv()

class TestCountDiv:
    MAX_INT = int(2e9)
    # INT_RANGE = (1, MAX_INT)

    def test_example(self, count_div):
        assert count_div.solution(6, 11, 2) == 3

    def test_small(self, count_div):
        assert count_div.solution(5, 11, 2), 3
        assert count_div.solution(6, 12, 2), 4
        assert count_div.solution(5, 12, 2), 4
        assert count_div.solution(5, 13, 2), 4

    def test_edges(self, count_div):
        assert count_div.solution(0, 0, 1) == 1
        assert count_div.solution(0, 1, 1) == 2
        assert count_div.solution(1, 1, 2) == 0
        assert count_div.solution(10, 20, 10) == 2
        assert count_div.solution(9, 21, 10) == 2

    def test_max_min(self, count_div):
        assert count_div.solution(0, self.MAX_INT, 1) == self.MAX_INT + 1
