
import pytest
import random

from python_algorithms.problems.codility.time_complexity.perm_missing_elem import PerMissElem

@pytest.fixture
def perm_missing_elem():
    return PerMissElem()

class TestPerMissElem:
    INT_RANGE = (0, 100000)
    def test_example1(self, perm_missing_elem):
        assert perm_missing_elem.solution([2,3,1,5]) == 4

    def test_single(self, perm_missing_elem):
        assert perm_missing_elem.solution([2]) == 1
        assert perm_missing_elem.solution([1]) == 2

    def test_random(self, perm_missing_elem):
        arr = [n for n in range(1, random.randint(*self.INT_RANGE))]
        missing =  random.randint(0, len(arr))
        arr.remove(missing)

        assert perm_missing_elem.solution(arr) == missing

    def test_maximum(self, perm_missing_elem):
        arr = [n for n in range(1, self.INT_RANGE[1]+1)]
        arr.pop()
        assert perm_missing_elem.solution(arr) == self.INT_RANGE[1]
