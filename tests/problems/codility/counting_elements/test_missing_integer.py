
import pytest

from python_algorithms.problems.codility.counting_elements.missing_integer import MissingInteger

@pytest.fixture
def missing_integer():
    return MissingInteger()

class TestMissingInteger:

    def test_example(self, missing_integer):
        X = [1, 3, 6, 4, 1, 2]
        assert missing_integer.solution(X) == 5

    def test_extreme_single(self, missing_integer):
        assert missing_integer.solution([2]) == 1
        assert missing_integer.solution([1]) == 2
        assert missing_integer.solution([-1]) == 1

    def test_simple(self, missing_integer):
        assert missing_integer.solution([2,3,4,6,10,1000]) == 1
        assert missing_integer.solution([-1, 0, 1, 2, 3, 4, 5, 6, 10, 1000]) == 7
        assert missing_integer.solution([1000, -1, 10, 3, -5, 2, 11, 59, 1]) == 4

    def test_extreme_min_max_int(self, missing_integer):
        assert missing_integer.solution([MissingInteger.ELEMENT_RANGE[0], MissingInteger.ELEMENT_RANGE[1], -10]) == 1

    # def test_positive_only(self):
    #     arr = range(1, 101) + range(102, 201)
    #     random.shuffle(arr)
    #     assert self.missing_integer.solution(arr), 101)

    # def test_negative_only(self):
    #     arr = range(-100, 0)
    #     random.shuffle(arr)
    #     assert self.missing_integer.solution(arr), 1)

    def test_no_gaps(self, missing_integer):
        assert missing_integer.solution([1, 2, 3, 4, 5]) == 6

    def test_duplicates(self, missing_integer):
        assert missing_integer.solution([1, 1, 1, 3, 3, 3]) == 2

    # def test_large_2(self):
    #     # create big array of ints
    #     arr = range(1,100000)
    #     random.shuffle(arr)
    #     # remove one
    #     missing_idx = random.randint(1, len(arr))
    #     missing_int = arr[missing_idx]
    #     del arr[missing_idx]
    #     # run it
    #     assert self.missing_integer.solution(arr) == missing_int

    # def test_monster_positive(self, missing_integer):
    #     arr = [random.randint(*MissingInteger.ELEMENT_RANGE) for _ in range(1, MissingInteger.N_RANGE[1])]
    #     random.shuffle(arr)
