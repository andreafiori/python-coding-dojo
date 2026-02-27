"""
https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
    Input: nums = [3,2,3]
    Output: [3]

Example 2:
    Input: nums = [1]
    Output: [1]

Example 3:
    Input: nums = [1,2]
    Output: [1,2]

Constraints:
    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109

"""

class MajorityElementII
    def solution(self, nums):
        # O(1) space
        ls = len(nums)
        res = []
        check_value = []
        for i in range(ls):
            if nums[i] in check_value:
                continue
            count = 1
            for j in range(i + 1, ls):
                if nums[i] == nums[j]:
                    count += 1
            if count > ls / 3:
                res.append(nums[i])
            check_value.append(nums[i])
        return res

    # def majorityElement(self, nums):
    #     # using dict
    #     count_hash = {}
    #     res = []
    #     for i in nums:
    #         try:
    #             count_hash[i] += 1
    #         except KeyError:
    #             count_hash[i] = 1
    #     for k, v in count_hash.iteritems():
    #         if v > len(nums) / 3:
    #             res.append(k)
    #     return res

    # def majorityElement(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[int]
    #     """
    #     #https://leetcode.com/discuss/76542/easy-python-solution
    #     tmp = {}
    #     res = []
    #     for n in list(set(nums)):
    #         tmp[n] = nums.count(n)
    #     for k, v in tmp.iteritems():
    #         if v > len(nums) / 3:
    #             res.append(k)
    #     return res