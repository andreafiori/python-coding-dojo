import pytest

from python_algorithms.problems.leetcode.ltc_0954_array_of_doubled_pairs import ArrayOfDoubledPairs

@pytest.fixture
def array_doubled_pairs():
    """Provide a fresh ArrayOfDoubledPairs instance for each test."""
    return ArrayOfDoubledPairs()

class TestArrayOfDoubledPairs:

    def test_can_reorder_doubled_false_case1(self, array_doubled_pairs):
        assert not array_doubled_pairs.can_reorder_doubled([3, 1, 3, 6])

    def test_can_reorder_doubled_false_case2(self, array_doubled_pairs):
        assert not array_doubled_pairs.can_reorder_doubled([2, 1, 2, 6])

    def test_can_reorder_doubled_false_case3(self, array_doubled_pairs):
        assert not array_doubled_pairs.can_reorder_doubled([1, 2, 4, 16, 8, 4])

    def test_can_reorder_doubled_true_case(self, array_doubled_pairs):
        assert array_doubled_pairs.can_reorder_doubled([4, -2, 2, -4])
