"""
Tape Equilibrium | http://codility.com/demo/take-sample-test/tape_equilibrium

The variable of head stores the sum of the heading part of the tape. And the variable of tail stores the sum of tailing part.

Then, we move the index from 2nd position to the last 2nd position.

Every time we move the index, we adjust both head and tail, compute and compare the difference.

"""

class TapeEquilibrium:
    def solution(self, A):
        """
        Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
        :param A: non-empty list of integers
        :return: minimal difference between two partitions
        """
        if len(A) < 2:
            raise ValueError("Array must contain at least two elements")

        before = A[0]
        after = sum(A) - A[0]
        best = abs(before - after)

        for P in range(1, len(A) - 1):
            before += A[P]
            after -= A[P]
            best = min(best, abs(before - after))

        return best
