
class PerMissElem:
    INT_RANGE = (0, 100000)

    def solution(self, A: list[int]) -> int:
        """
        Find the missing element in a given permutation
        :param A: list of integers
        :return: the integer that is missing in O(n) time and O(1) space complexity
        """
        if len(A) == 0:
            return 1

        return sum(range(1, len(A)+2)) - sum(A)
