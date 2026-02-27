"""
https://leetcode.com/problems/ugly-number-ii/description/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
    Input: n = 10
    Output: 12
    Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
    Input: n = 1
    Output: 1
    Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Constraints:
    1 <= n <= 1690

"""

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        dp = [0] * (n + 1)
        l1 = l2 = l3 = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        dp[5] = 5
        for i in range(6, n + 1):
            while dp[l1] * 2 <= dp[i - 1]:
                l1 += 1
            while dp[l2] * 3 <= dp[i - 1]:
                l2 += 1
            while dp[l3] * 5 <= dp[i - 1]:
                l3 += 1
            print(l1, l2, l3)
            dp[i] = min(dp[l1] * 2, dp[l2] * 3, dp[l3] * 5)
        # print dp
        return dp[n]
