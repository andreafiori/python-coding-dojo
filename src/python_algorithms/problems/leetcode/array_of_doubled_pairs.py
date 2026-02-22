"""
Array Of Doubled Pairs

URL https://leetcode.com/problems/array-of-doubled-pairs/

Given an array of integers A with even length, return true if and only if it is possible to reorder it
 such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

Example 1:
    Input: [3,1,3,6]
    Output: false

Example 2:
    Input: [2,1,2,6]
    Output: false

Example 3:
    Input: [4,-2,2,-4]
    Output: true
    Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:
    Input: [1,2,4,16,8,4]
    Output: false

Note:
    0 <= A.length <= 30000
    A.length is even
    -100000 <= A[i] <= 100000

"""


class ArrayOfDoubledPairs(object):
    def can_reorder_doubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        v_map = {}
        arr.sort(key=lambda x: abs(x))
        for n in arr:
            v_map[n] = v_map.get(n, 0) + 1
        for n in arr:
            if v_map[n] <= 0:
                continue
            if 2 * n in v_map and v_map[2 * n] > 0:
                v_map[n] -= 1
                v_map[2 * n] -= 1
            else:
                return False
        return True
