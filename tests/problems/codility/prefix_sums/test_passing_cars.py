import pytest
import random

from python_algorithms.problems.codility.prefix_sums.passing_cars import PassingCars

@pytest.fixture
def passing_cars():
    """Provide a fresh PassingCars instance for each test."""
    return PassingCars()

class TestPassingCars:
    def test_solution_is_zero(self, passing_cars):
        assert passing_cars.solution([0]) == 0
        assert passing_cars.solution([1]) == 0
        assert passing_cars.solution([0, 0]) == 0
        assert passing_cars.solution([1, 1]) == 0
        assert passing_cars.solution([1, 0]) == 0
        assert passing_cars.solution([0, 0, 0]) == 0
        assert passing_cars.solution([1, 0, 0]) == 0
        assert passing_cars.solution([1, 1, 0]) == 0
        assert passing_cars.solution([1, 1, 1]) == 0
        assert passing_cars.solution([1, 0, 0, 0]) == 0
        assert passing_cars.solution([1, 1, 0, 0]) == 0
        assert passing_cars.solution([1, 1, 1, 0]) == 0
        assert passing_cars.solution([1, 1, 1, 1]) == 0
        assert passing_cars.solution([0, 0, 0, 0]) == 0

    def test_solution_is_one(self, passing_cars):
        assert passing_cars.solution([0, 1]) == 1
        assert passing_cars.solution([0, 1, 0]) == 1
        assert passing_cars.solution([1, 0, 1]) == 1
        assert passing_cars.solution([0, 1, 0, 0]) == 1
        assert passing_cars.solution([1, 1, 0, 1]) == 1
        assert passing_cars.solution([1, 0, 1, 0]) == 1

    def test_solution_is_two(self, passing_cars):
        assert passing_cars.solution([0, 1, 1]) == 2
        assert passing_cars.solution([1, 0, 0, 1]) == 2
        assert passing_cars.solution([1, 0, 1, 1]) == 2

    def test_solution_is_three(self, passing_cars):
        assert passing_cars.solution([0, 0, 0, 1]) == 3
        assert passing_cars.solution([0, 1, 0, 1]) == 3
        assert passing_cars.solution([0, 1, 1, 1]) == 3

    def test_solution_is_four(self, passing_cars):
        assert passing_cars.solution([0, 0, 1, 1]) == 4

    def test_solution_is_five(self, passing_cars):
        assert passing_cars.solution([0, 1, 0, 1, 1]) == 5

    def test_extreme(self, passing_cars):
        assert passing_cars.solution([random.randint(0,1) for _ in range(int(1e6))]) == -1
