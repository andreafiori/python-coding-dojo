"""

https://leetcode.com/problems/ugly-number/description/

An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
    Input: n = 6
    Output: true
    Explanation: 6 = 2 × 3

Example 2:
    Input: n = 1
    Output: true
    Explanation: 1 has no prime factors.

Example 3:
    Input: n = 14
    Output: false
    Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
    -231 <= n <= 231 - 1

"""

class Solution:
    # def isUgly(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     if num <= 0:
    #         return False
    #     if num <= 6:
    #         return True
    #     while num % 2 == 0:
    #         num //= 2
    #     while num % 3 == 0:
    #         num //= 3
    #     while num % 5 == 0:
    #         num //= 5
    #     if num == 1:
    #         return True
    #     return False
    def isUgly(self, num):
        if num <= 0:
            return False
        divisors = [2, 3, 5]
        for d in divisors:
            while num % d == 0:
                num /= d
        return num == 1

# if __name__ == '__main__':
#     s = Solution()
#     print s.isUgly(-2147483648)
