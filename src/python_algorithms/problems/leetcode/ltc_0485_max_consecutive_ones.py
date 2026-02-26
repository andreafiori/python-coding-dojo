"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
    Input: nums = [1,1,0,1,1,1]

    Output: 3

    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
    Input: nums = [1,0,1,1,0,1]
    Output: 2

Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.

"""

from typing import List

class FindMaxConsecutiveOnes(object):
    def solution(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        curr = 0
        for n in nums:
            if n == 1:
                # Add 1 to curr when encounter 1
                curr += 1
                if curr > ans:
                    ans = curr
            else:
                # Add 1 to curr when encounter 1
                curr = 0
        return ans
