"""
https://leetcode.com/problems/3sum/description/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

Example 2:
    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.

Constraints:
    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

Hint 1:
    So, we essentially need to find three numbers x, y, and z such that they add up to the given value. If we fix one of the numbers say x, we are left with the two-sum problem at hand!

Hint 2:
    For the two-sum problem, if we fix one of the numbers, say x, we have to scan the entire array to find the next number y, which is value - x where value is the input parameter. Can we change our array somehow so that this search becomes faster?

Hint 3:
    The second train of thought for two-sum is, without changing the array, can we use additional space somehow? Like maybe a hash map to speed up the search?

"""

class ThreeSum
    # def threeSum(self, nums):
    #     # skip duplicate
    #     # O(n^3)
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     ls = len(nums)
    #     result = []
    #     for i in range(0, ls - 2):
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i - 1]:
    #             continue
    #         j = i + 1
    #         k = ls - 1
    #         while(j < k):
    #             temp = [nums[i], nums[j], nums[k]]
    #             s = sum(temp)
    #             jtemp = nums[j]
    #             ktemp = nums[k]
    #             if s <= 0:
    #                 j += 1
    #                 while(j < k and jtemp == nums[j]):
    #                     j += 1
    #                 if s == 0:
    #                     result.append(temp)
    #             else:
    #                 k -= 1
    #                 while(j < k and ktemp == nums[k]):
    #                     k -= 1
    #     return result

    # def threeSum(self, nums):
    #     """
    #         :type nums: List[int]
    #         :rtype: List[List[int]]
    #     """
    #     # using multiple 2 sum
    #     nums.sort()
    #     result, visited = set(), {}
    #     for i in range(len(nums) - 2):
    #         table, target = {}, -nums[i]
    #         if nums[i] not in visited:
    #             for j in range(i + 1, len(nums)):
    #                 if nums[j] not in table:
    #                     table[target - nums[j]] = j
    #                 else:
    #                     result.add((nums[i], target - nums[j], nums[j]))
    #             visited[nums[i]] = 1
    #     return list(result)

    def solution_one(self, nums):
        res = []
        nums.sort()
        ls = len(nums)
        for i in range(ls - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = ls - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                else:
                    k -= 1
        return res

    def solution_two(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        N = len(nums)
        triplets = []
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            ptrL = i + 1
            ptrR = N - 1
            while ptrL < ptrR:
                s = nums[i] + nums[ptrL] + nums[ptrR]
                if s > 0:
                    ptrR -= 1
                elif s < 0:
                    ptrL += 1
                else:
                    triplets.append([nums[i], nums[ptrL], nums[ptrR]])
                    ptrL += 1
                    while nums[ptrL] == nums[ptrL - 1] and ptrL < ptrR:
                        ptrL += 1

        return triplets