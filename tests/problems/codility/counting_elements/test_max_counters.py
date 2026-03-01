import pytest

from python_algorithms.problems.codility.counting_elements.max_counters import MaxCounters

@pytest.fixture
def max_counter():
    return MaxCounters()

class TestMaxCounters:
    def test_solution(self, max_counter):
        pass
