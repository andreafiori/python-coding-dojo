"""
Single Number

URL: https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1
Example 2:
    Input: [4,1,2,1,2]
    Output: 4

"""
class SingleNumber(object):
    # def solution(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # hash
    #     dic = {}
    #     for num in nums:
    #         try:
    #             dic[num] += 1
    #         except KeyError:
    #             dic[num] = 1
    #     for num in nums:
    #         if dic[num] == 1:
    #             return num

    # def singleNumber(self, nums):
    #     # set
    #     s = set()
    #     for num in nums:
    #         if num in s:
    #             s.remove(num)
    #         else:
    #             s.add(num)
    #     return s.pop()

    def solution(self, nums):
        """
        Solution
        :param nums:
        :return:
        """
        # xor
        res = 0
        for num in nums:
            res ^= num
        return res