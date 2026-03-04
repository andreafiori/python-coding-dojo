"""
Candy | https://leetcode.com/problems/candy/

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104

"""

from typing import List

class Candy:
    def candy(self, ratings: List[int]) -> int:
        """
        https://discuss.leetcode.com/topic/5243/a-simple-solution
        :type ratings: List[int]
        :rtype: int
        """
        if ratings is None or len(ratings) == 0:
            return 0
        ls = len(ratings)
        num = [1] * ls
        for i in range(1, ls):
            if ratings[i] > ratings[i - 1]:
                num[i] = num[i - 1] + 1
        for i in range(ls - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                num[i - 1] = max(num[i] + 1, num[i - 1])
        return sum(num)
