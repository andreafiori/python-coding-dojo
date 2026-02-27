"""
"""

class FindPeakElement:
    def find(self, nums):
        # https://leetcode.com/discuss/88467/tricky-problem-tricky-solution
        # note that num[-1] = num[n] = -∞
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) / 2
            if nums[mid] < nums[mid+1]:
                start= mid + 1
            else:
                end = mid
        return start

    #     def find(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         """