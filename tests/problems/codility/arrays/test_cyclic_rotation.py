import pytest

from src.python_algorithms.problems.codility.arrays.cyclic_rotation import CyclicRotation

@pytest.fixture
def cyclic_rotation():
    return CyclicRotation()

class TestCyclicRotation:

    def test_zero(self, cyclic_rotation):
        assert cyclic_rotation.rotate([6, 3, 8, 9, 7], 0) == [6, 3, 8, 9, 7]

    def test_one(self, cyclic_rotation):
        assert cyclic_rotation.rotate([6, 3, 8, 9, 7], 1) == [7, 6, 3, 8, 9]

    def test_example1(self, cyclic_rotation):
        assert cyclic_rotation.rotate([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]

    def test_full(self, cyclic_rotation):
        assert cyclic_rotation.rotate([6, 3, 8, 9, 7], 5) == [6, 3, 8, 9, 7]

    def test_empty(self, cyclic_rotation):
        assert cyclic_rotation.rotate([], 5), []

    # def test_random(self):
    #     ARRAY_RANGE = (-1000, 1000)
    #     INT_RANGE = (0, 100)
    #     N = random.randint(*INT_RANGE)
    #     K = random.randint(*INT_RANGE)
    #     A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
