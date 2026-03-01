"""
MaxProductOfThree

Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R)

https://codility.com/programmers/task/max_product_of_three/
----------------
# My Commentary

The 'trick' with this one is to realise that two negatives make a positive. Sorting the array then multiplying the
three biggest math will only get you a score of 44%.

You have to include a branch in the code to accommodate two big negative math combining with
a positive number to provide a greater product than multiplying the positives together.

eg:
[-100, -100, -100, 0, 50, 50, 50]
The product of the top 3 is 125000, but the product of the bottom two (-100, 100)
 with the top one (50) is 500000!


-------------------
# Problem Description


A non-empty zero-indexed array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 <= P < Q < R < N).

For example, array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

contains the following example triplets:

        (0, 1, 2), product is -3 * 1 * 2 = -6
        (1, 2, 4), product is 1 * 2 * 5 = 10
        (2, 4, 5), product is 2 * 5 * 6 = 60

Your goal is to find the maximal product of any triplet.

Write a function:

    def solution(A)

that, given a non-empty zero-indexed array A, returns the value of the maximal product of any triplet.

For example, given array A such that:
  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6

the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Assume that:

        N is an integer within the range [3..100,000];
        each element of array A is an integer within the range [-1,000..1,000].

Complexity:

        expected worst-case time complexity is O(N*log(N));
        expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).

Elements of input arrays can be modified.
"""

import unittest
import random

class MaxProductOfThree:

    RANGE_A = (-1000, 1000)
    RANGE_N = (3, 100000)

    def solution(self, A):
        """
        :param A: array of integers
        :return: an integer
        """
        # sort them, then just use the last three!
        A.sort()
        if A[0] < 0 and A[1] < 0 and A[-1] > 0:
            # excepting that two negatives make a positive...
            return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
        else:
            return A[-3] * A[-2] * A[-1]

