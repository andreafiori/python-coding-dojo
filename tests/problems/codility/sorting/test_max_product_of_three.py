import pytest

class TestMaxProductOfThree:
    def test_example(self):
        assert solution([-3, 1, 2, -2, 5, 6]), 60)

    def test_sample(self):
        assert solution([-5, 5, -5, 4]), 125)

    def test_zero(self):
        assert solution([0, 0, 0, 0]), 0)
        assert solution([-10, -10, -3, 0, 1]), 100)

    def test_negative(self):
        assert solution([-4, -3, -2, -1]), -6)
        assert solution([-1, -1, 1, 2]), 2)
        assert solution([-5, -5, 1, 2]), 50)
        assert solution([-5, -5, -1, 0]), 0)

    def test_large(self):
        assert solution([1000, 1000, 1000]), int(1e9))

    def test_extreme(self):
        A = [random.randint(*RANGE_A) for _ in range(3, 99997)]
        A += [1000, 1000, 1000]
        assert solution(A), int(1e9))
