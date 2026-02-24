"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/

"""

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i=0
        j=0
        output = []
        nums1.sort()
        nums2.sort()

        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i = i+1
            elif nums1[i] > nums2[j]:
                j = j+1
            else:
                output.append(nums1[i])
                i=i+1
                j=j+1

        return output
