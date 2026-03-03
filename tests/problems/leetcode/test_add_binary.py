import pytest

from python_algorithms.problems.leetcode.ltc_0067_add_binary import AddBinary

@pytest.fixture
def add_binary():
    """Provide a fresh AddBinary instance for each test."""
    return AddBinary()

class TestAddBinary:
    def test_solution(self, add_binary):
        assert add_binary.solution_one("11", "1") == "100"
