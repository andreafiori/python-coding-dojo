"""
Single Number II

URL: https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,3,2]
    Output: 3

Example 2:
    Input: [0,1,0,1,0,1,99]
    Output: 99

"""
class SingleNumberII(object):
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     import ctypes
    #     # note that if res is not c 32
    #     # there will be errors
    #     count = [0] * 32
    #     res = ctypes.c_int32(0)
    #     for i in range(32):
    #         for num in nums:
    #             if (ctypes.c_int32(num).value >> i) & 1:
    #                 count[i] += 1
    #         res.value |= ((count[i] % 3) << i)
    #     return res.value

    def solution(self, nums):
        """
        Solution 2
        :param nums: int
        :return: int
        """
        # bitmask
        # ones as a bitmask to represent the ith bit had appeared once.
        # twos as a bitmask to represent the ith bit had appeared twice.
        # threes as a bitmask to represent the ith bit had appeared three times.
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones