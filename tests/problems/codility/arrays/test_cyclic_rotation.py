import pytest

from python_algorithms.problems.codility.arrays.cyclic_rotation import CyclicRotation

@pytest.fixture
def cyclic_rotation():
    return CyclicRotation()

class TestCyclicRotation:

    def test_zero(self, cyclic_rotation):
        A = [6, 3, 8, 9, 7]
        assert cyclic_rotation.rotate(A, 0) == A

    def test_one(self, cyclic_rotation):
        A = [6, 3, 8, 9, 7]
        assert cyclic_rotation.rotate(A, 1) == [7, 6, 3, 8, 9]

    def test_example1(self, cyclic_rotation):
        X = [3, 8, 9, 7, 6]
        assert cyclic_rotation.rotate(X, 3) == [9, 7, 6, 3, 8]

    def test_full(self, cyclic_rotation):
        X = [6, 3, 8, 9, 7]
        assert cyclic_rotation.rotate(X, 5) == [6, 3, 8, 9, 7]

    def test_empty(self, cyclic_rotation):
        empty = []
        assert cyclic_rotation.rotate(empty, 5) == []

    # def test_random(self):
    #     ARRAY_RANGE = (-1000, 1000)
    #     INT_RANGE = (0, 100)
    #     N = random.randint(*INT_RANGE)
    #     K = random.randint(*INT_RANGE)
    #     A = [random.randint(*ARRAY_RANGE) for i in range(0, N)]
