import pytest

from src.python_algorithms.problems.codility.prefix_sums.count_div import CountDiv

@pytest.fixture
def count_div():
    return CountDiv()

class TestCountDiv:
    def test_solution(self, count_div):
        assert count_div.solution([0]) == 0
