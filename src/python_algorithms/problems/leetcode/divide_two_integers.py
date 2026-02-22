# class Solution(object):
#     def divide(self, dividend, divisor):
#         """
#         :type dividend: int
#         :type divisor: int
#         :rtype: int
#         """

import math


class Solution(object):
    MAX_INT = int(100000)

    def divide(self, dividend, divisor):
        if divisor == 0:
            return self.MAX_INT
        if dividend == 0:
            return 0
        isPositive = (dividend < 0) == (divisor < 0)
        m = abs(dividend)
        n = abs(divisor)
        # ln and exp
        res = math.log(m) - math.log(n)
        res = int(math.exp(res))
        if isPositive:
            return min(res, 2147483647)
        return max(0 - res, -2147483648)

    # def divide(self, dividend, divisor):
    #     # (dividend >= 0) ^ (divisor < 0)
    #     isPositive = (dividend < 0) == (divisor < 0)
    #     dividend, divisor, result = abs(dividend), abs(divisor), 0
    #     while dividend >= divisor:
    #         n, nb = 1, divisor
    #         # fast minus
    #         while dividend >= nb:
    #             dividend, result = dividend - nb, result + n
    #             n, nb = n << 1, nb << 1
    #     if isPositive:
    #         return min(result, 2147483647)
    #     return max(-result, -2147483648)

"""
s = Solution()
print s.divide(1, 1)
"""
