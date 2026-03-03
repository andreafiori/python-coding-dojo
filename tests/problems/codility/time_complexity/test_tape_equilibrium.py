import pytest

from python_algorithms.problems.codility.time_complexity.tape_equilibrium import TapeEquilibrium

@pytest.fixture
def tape_equilibrium():
    return TapeEquilibrium()

class TestTapeEquilibrium:
    N_RANGE = (2, 100000)
    ELEMENT_RANGE = (-1000, 1000)

    def test_example1(self, tape_equilibrium):
        assert tape_equilibrium.solution([3, 1, 2, 4, 3]) == 1

    def test_simple(self, tape_equilibrium):
        assert tape_equilibrium.solution([1,2]) == 1

    def test_double(self, tape_equilibrium):
        assert tape_equilibrium.solution([-1000, 1000]) == 2000

    # def test_random(self, tape_equilibrium):
    #     N = random.randint(*self.N_RANGE)
    #     arr = [random.randint(*self.ELEMENT_RANGE) for _ in range(N)]

    # def test_maximum(self, tape_equilibrium):
    #     arr = [random.randint(*TapeEquilibrium.ELEMENT_RANGE) for _ in range(100000)]
