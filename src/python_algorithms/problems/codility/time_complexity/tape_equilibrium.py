"""
Tape Equilibrium

URL: http://codility.com/demo/take-sample-test/tape_equilibrium

The variable of head stores the sum of the heading part of the tape. And the variable of tail stores the sum of tailing part.
 Then, we move the index from 2nd position to the last 2nd position.
 Every time we move the index, we adjust both head and tail, compute and compare the difference.
"""
class TapeEquilibrium(object):

    N_RANGE = (2, 100000)
    ELEMENT_RANGE = (-1000, 1000)

    @staticmethod
    def solution(A):
        """
        Minimize the value |(A[0] + ... + A[P-1]) = (A[P] + ... + A[N-1])|.
        :param A: non-empty list of integers
        :return: an integer - the index value where the smallest difference occurs
        """
        # array must be more than 2 elements
        assert len(A) > 1

        # establish the tallys
        best = None
        before = 0
        after = sum(A)

        # adjust and test at every split
        for P in range(0, len(A) - 1):
            before += A[P]
            after -= A[P]
            difference = abs(before - after)
            if best is None or difference < best:
                best = difference

        return best

