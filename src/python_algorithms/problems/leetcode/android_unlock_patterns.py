"""
https://leetcode.com/problems/android-unlock-patterns/

Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of
unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

Rules for a valid pattern:
- Each pattern must connect at least m keys and at most n keys.
- All the keys must be distinct.
- If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have
previously selected in the pattern. No jumps through non selected key is allowed.
- The order of keys used matters.

https://medium.com/@rebeccahezhang/leetcode-351-android-unlock-patterns-d9bae4a8a958

"""


class AndroidUnlockPatterns(object):
    def solution(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        used = [False] * 9
        res = 0
        for l in range(m, n + 1):
            res += self.calc_patterns(used, -1, l)
            used = [False] * 9
        return res

    def is_valid(self, used, index, last):
        """
        Check if inputs are valid
        :param used:
        :param index:
        :param last:
        :return:
        """
        # markded
        if used[index]:
            return False
        # first digit
        if last == -1:
            return True
        # adjacent cells (in a row or in a column)
        if (last + index) % 2 == 1:
            return True
        mid = (last + index) / 2
        if mid == 4:
            return used[mid]
        # adjacent cells on diagonal
        if (index % 3 != last % 3) and (index / 3 != last / 3):
            return True
        # all other cells which are not adjacent
        return used[mid]

    def calc_patterns(self, used, last, length):
        if length == 0:
            return 1
        res = 0
        for i in range(9):
            if self.is_valid(used, i, last):
                used[i] = True
                res += self.calc_patterns(used, i, length - 1)
                used[i] = False
        return res
