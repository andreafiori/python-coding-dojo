
import pytest

from src.python_algorithms.problems.codility.sorting.triangle import Triangle

@pytest.fixture
def triangle_instance():
    return Triangle()

class TestTriangle:
    # RANGE_A = (-2147483648, 2147483647)
    RANGE_N = (0, 100000)

    def test_example(self, triangle_instance):
        assert triangle_instance.solution([10, 2, 5, 1, 8, 20]) == 1
        assert triangle_instance.solution([10, 50, 5, 1]) == 0

    def test_lowballs(self, triangle_instance):
        # empty = []
        zero = [0]
        couple = [0, 1]
        # assert triangle_instance.solution(empty) == 0
        assert triangle_instance.solution(zero) == 0
        assert triangle_instance.solution(couple) == 0

    def test_simple(self, triangle_instance):
        A = [5, 3, 3]
        assert triangle_instance.solution(A) == 1

    # def test_large_negative(self, triangle_instance):
    #     assert triangle_instance.solution([-1] * self.RANGE_N[1]) == 0
