"""
Add binary

https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"


Constraints:
    Each string consists only of '0' or '1' characters.
    1 <= a.length, b.length <= 10^4
    Each string is either "0" or doesn't contain any leading zero.

"""


class AddBinary(object):
    @staticmethod
    def solution(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        lsa, lsb = len(a), len(b)
        pos = -1
        plus = 0
        while (lsa + pos) >= 0 and (lsb + pos) >= 0:
            curr = int(a[pos]) + int(b[pos]) + plus
            if curr >= 2:
                plus = 1
                curr %= 2
            else:
                plus = 0
            res = str(curr) + res
            pos -= 1
        if lsa + pos >= 0:
            while (lsa + pos) >= 0:
                curr = int(a[pos]) + plus
                if curr >= 2:
                    plus = 1
                    curr %= 2
                else:
                    plus = 0
                res = str(curr) + res
                pos -= 1
        if lsb + pos >= 0:
            while (lsb + pos) >= 0:
                curr = int(b[pos]) + plus
                if curr >= 2:
                    plus = 1
                    curr %= 2
                else:
                    plus = 0
                res = str(curr) + res
                pos -= 1
        if plus == 1:
            res = '1' + res
        return res
