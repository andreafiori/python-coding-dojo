"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step


Climbing Stairs: Time - O(n), space: O(n)
Let's say your goal is level 6. Try to think the possible ways of reaching level 6. One way is to jump 2 steps from level 4. Other way is to jump 1 step from level 5. So you can reach level 6 from either level 4 or level 5. For this to happen, you have to be in those levels first, and hence we need to calculate possible ways to reach those levels.

Ways to reach level 6 = ways to reach level 4 + ways to reach level 5
You might think - I can also take 1 step + 1 step from level 4. But when you take the initial 1 step from level 4, you would reach level 5. And this case was already counted in the 'ways to reach level 5'. So need not think about 1 step + 1 step in this approach.

Similar approach has to be followed for levels 4 and 5 till you reach base cases.

Base cases: With the data given, we can easily say the ways to reach level 1 = 1; and the ways to reach level 2 = 2 (jumps of 1 step + 1 step, jump of 2 steps).

The question reduces to fibonacci sequence with starting digits being 1 and 2.
"""
class ClimbStairs(object):
    def solution_one(self, n: int) -> int:
        """
        :param n: int
        :return: int
        """
        if n < 0 or n == 0:
            return 0

        if n == 1 or n == 2:
            return n

        n_minus_two_step, n_minus_one_step = 1, 2

        for i in range(3, n + 1):
            n_minus_two_step, n_minus_one_step = n_minus_one_step, n_minus_two_step + n_minus_one_step

        return n_minus_one_step

    def solution_two(self, n: int) -> int:
        one, two = 1,1
        for i in range (n-1):
            temp = one
            one = one +two
            two = temp
        return one