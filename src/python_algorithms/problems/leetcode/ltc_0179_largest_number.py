"""
Largest Number | https://leetcode.com/problems/largest-number/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Example 1:
    Input: nums = [10,2]
    Output: "210"

Example 2:
    Input: nums = [3,30,34,5,9]
    Output: "9534330"

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9

"""

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class LargestNumber:
    def find_largest_number(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
