"""
https://leetcode.com/problems/add-digits/

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2
    Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
                 Since 2 has only one digit, return it.

Wikipedia: https://en.wikipedia.org/wiki/Digital_root

"""


def add_digits(num: int) -> int:
    """
    Add digits
    :type num: int
    :rtype: int
    """
    while num // 10 >= 1:
        num = sum([int(x) for x in str(num)])
    return num
