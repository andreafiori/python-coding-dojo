"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Question: https://leetcode.com/problems/maximum-subarray/
"""

from typing import List

class Solution(object):
    def solution_one(self, nums):
        maxEndingHere = maxSofFar = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSofFar = max(maxEndingHere, maxSofFar)
        return maxSofFar

    def solution_two(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum <0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub