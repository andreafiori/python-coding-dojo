import pytest

from src.python_algorithms.problems.codility.counting_elements.frog_river_one import FrogRiverOne

@pytest.fixture
def frog_river_one():
    return FrogRiverOne()

class TestfrogRiverOne:
    def test_example_case(self, frog_river_one):
        X = 5
        A = [1, 3, 1, 4, 2, 3, 5, 4]
        assert frog_river_one.solution(X, A) == 6

    def test_frog_never_crosses(self, frog_river_one):
        X = 5
        A = [1, 1, 1, 1]  # never covers positions 2,3,4,5
        assert frog_river_one.solution(X, A) == -1

    def test_all_leaves_same_position(self, frog_river_one):
        X = 3
        A = [2, 2, 2, 2]
        assert frog_river_one.solution(X, A) == -1

    def test_single_position_success(self, frog_river_one):
        X = 1
        A = [1]
        assert frog_river_one.solution(X, A) == 0

    # def test_single_position_failure():
    #     X = 1
    #     A = [2, 2, 2]  # invalid positions but still no 1
    #     assert FrogRiverOne.solution(X, A) == -1

    def test_random_small_case(self, frog_river_one):
        X = 3
        A = [3, 1, 2]
        # positions 1,2,3 all covered at second index 2
        assert frog_river_one.solution(X, A) == 2

    def test_large_case_permutation(self, frog_river_one):
        X = 5
        A = [5, 4, 3, 2, 1]
        # all positions covered at second index 4
        assert frog_river_one.solution(X, A) == 4
