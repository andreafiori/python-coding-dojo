import pytest

from src.python_algorithms.problems.codility.sorting.number_of_disc_intersections import NumberOfDiscIntersections

@pytest.fixture
def number_of_disc_intersections():
    return NumberOfDiscIntersections()

class TestNumberOfDiscIntersections:
    def test_example(self, number_of_disc_intersections):
        assert number_of_disc_intersections.solution([1, 5, 2, 1, 4, 0]) == 11

    def test_simple(self, number_of_disc_intersections):
        assert number_of_disc_intersections.solution([1, 1, 1]) == 3

    def test_extreme_small(self, number_of_disc_intersections):
        assert number_of_disc_intersections.solution([]) == 0
        assert number_of_disc_intersections.solution([10]) == 0
        assert number_of_disc_intersections.solution([1, 1]) == 1

    def test_extreme_large(self, number_of_disc_intersections):
        A = [10000000] * 100000
        assert number_of_disc_intersections.solution(A) == -1
