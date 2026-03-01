import pytest

from src.python_algorithms.problems.codility.time_complexity.tape_equilibrium import TapeEquilibrium

@pytest.fixture
def perm_missing_elem():
    return TapeEquilibrium()

class TestTapeEquilibrium:
    def test_solution(self, tape):
        pass