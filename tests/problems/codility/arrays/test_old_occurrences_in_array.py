import pytest

from src.python_algorithms.problems.codility.arrays.old_occurrences_in_array import OldOddOccurrences

@pytest.fixture
def perm_missing_elem():
    return OldOddOccurrences()

class TestOldOddOccurrences:
    def odd_occurrences(self, A):
        pass