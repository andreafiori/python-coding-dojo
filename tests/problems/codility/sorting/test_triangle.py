
import pytest

from src.python_algorithms.problems.codility.sorting.triangle import Triangle

@pytest.fixture
def triangle():
    return Triangle()

class TestTriangle:
    def test_example(self, triangle):
        assert triangle.solution([10, 2, 5, 1, 8, 20]) == 1
        assert triangle.solution([10, 50, 5, 1]) == 0

    def test_lowballs(self, triangle):
        assert triangle.solution([])
        assert triangle.solution([0]) == 0
        assert triangle.solution([0, 1]) == 0

    def test_simple(self, triangle):
        A = [5, 3, 3]
        assert triangle.solution(A) == 1

    def test_large_negative(self, triangle):
        assert triangle.solution([-1] * triangle.RANGE_N[1]) == 0
