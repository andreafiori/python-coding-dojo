"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Question: https://leetcode.com/problems/contains-duplicate/

"""

from typing import List

class ContainsDuplicate:
    def solution(self, nums: List[int]) -> bool:
      duplicates = {}
      for i in nums:
        if i in duplicates:
          return True
        else:
          duplicates[i] = 1
      return False
