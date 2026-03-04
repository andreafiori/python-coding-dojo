"""
Largest Palindrome Product | https://leetcode.com/problems/largest-palindrome-product/

Given an integer n, return the largest palindromic integer that can be represented as the product of two n-digits integers. Since the answer can be very large, return it modulo 1337.

Example 1:
    Input: n = 2
    Output: 987
    Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Example 2:
    Input: n = 1
    Output: 9

Constraints:
    1 <= n <= 8

"""

class LongestPalindromeProduct:
    # def largestPalindrome(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1:
    #         return 9
    #     upperBound = 10 ** n - 1
    #     lowerBound = upperBound / 10
    #     maxNum = upperBound * upperBound
    #     firstHalf = maxNum / (10 ** n)
    #     palindromFound = False
    #     palindrom = 0
    #     while not palindromFound:
    #         palindrom = int(str(firstHalf) + str(firstHalf)[::-1])
    #         for i in range(upperBound, lowerBound, -1):
    #             if i * i < palindrom:
    #                 break
    #             if palindrom % i == 0:
    #                 palindromFound = True
    #                 break
    #         firstHalf -= 1
    #     return palindrom % 1337

    def findLargestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        for a in range(2, 9 * 10 ** (n - 1)):
            hi = (10 ** n) - a
            lo = int(str(hi)[::-1])
            if a ** 2 - 4 * lo < 0:
                continue
            if (a ** 2 - 4 * lo) ** .5 == int((a ** 2 - 4 * lo) ** .5):
                return (lo + 10 ** n * (10 ** n - a)) % 1337
