
import random

class Solution:
    def findKthLargest(self, nums, k):
        # shuffle nums to avoid n*n
        random.shuffle(nums)
        return self._quickSelection(nums, 0, len(nums) - 1, len(nums) - k)

    def _quickSelection(self, nums, start, end, k):
        if start > end:
            return float('inf')
        pivot = nums[end]
        left = start
        for i in range(start, end):
            if nums[i] <= pivot:
                # swip left and i
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        nums[left], nums[end] = nums[end], nums[left]
        if left == k:
            return nums[left]
        elif left < k:
            return self._quickSelection(nums, left + 1, end, k)
        else:
            return self._quickSelection(nums, start, left - 1, k)
