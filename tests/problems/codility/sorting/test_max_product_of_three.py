import pytest

from python_algorithms.problems.codility.sorting.max_product_of_three import MaxProductOfThree

@pytest.fixture
def max_product_of_three():
    return MaxProductOfThree()

class TestMaxProductOfThree:
    def test_example(self, max_product_of_three):
        assert max_product_of_three.solution([-3, 1, 2, -2, 5, 6]) == 60

    def test_sample(self, max_product_of_three):
        assert max_product_of_three.solution([-5, 5, -5, 4]) == 125

    def test_zero(self, max_product_of_three):
        assert max_product_of_three.solution([0, 0, 0, 0]) == 0
        assert max_product_of_three.solution([-10, -10, -3, 0, 1]) == 100

    def test_negative(self, max_product_of_three):
        assert max_product_of_three.solution([-4, -3, -2, -1]) == -6
        assert max_product_of_three.solution([-1, -1, 1, 2]) == 2
        assert max_product_of_three.solution([-5, -5, 1, 2]) == 50
        assert max_product_of_three.solution([-5, -5, -1, 0]) == 0

    def test_large(self, max_product_of_three):
        assert max_product_of_three.solution([1000, 1000, 1000]) == int(1e9)

    def test_extreme(self, max_product_of_three):
        A = [max_product_of_three.random.randint(*max_product_of_three.RANGE_A) for _ in range(3, 99997)]
        A += [1000, 1000, 1000]
        assert max_product_of_three.solution(A) == int(1e9)
