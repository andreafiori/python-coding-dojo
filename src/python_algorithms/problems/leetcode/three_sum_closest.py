"""
Three sum closest

URL https://leetcode.com/problems/3sum-closest/

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
    Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


def three_sum_closest(nums, target):
    """
    Three sum closest
    :param nums:
    :param target:
    :return:
    """
    ls = len(nums)
    sort_nums = sorted(nums)
    res = nums[0] + nums[1] + nums[2]
    for i in range(ls - 2):
        j, k = i + 1, ls - 1
        while j < k:
            temp = sort_nums[i] + sort_nums[j] + sort_nums[k]
            if abs(target - temp) < abs(target - res):
                res = temp
            if temp < target:
                j += 1
            else:
                k -= 1
    return res

#     def three_sum_closest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """