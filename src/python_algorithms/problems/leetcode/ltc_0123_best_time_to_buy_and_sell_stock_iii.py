"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
    Input: prices = [3,3,5,0,0,3,1,4]
    Output: 6
    Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
    Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
    Input: prices = [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
    Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
    1 <= prices.length <= 105
    0 <= prices[i] <= 105

https://discuss.leetcode.com/topic/50360/python-dp-and-non-dp-solution
"""

class BestTimeToBuyAndSellStock:
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     # https://discuss.leetcode.com/topic/4766/a-clean-dp-solution-which-generalizes-to-k-transactions
    #     ls = len(prices)
    #     if ls == 0:
    #         return 0
    #     num_t, max_profit = 2, 0
    #     dp = [[0] * ls for _ in range(num_t + 1)]
    #     for t in range(1, num_t + 1):
    #         tempMax = dp[t - 1][0] - prices[0]
    #         for i in range(1, ls):
    #             dp[t][i] = max(dp[t][i - 1], prices[i] + tempMax)
    #             tempMax = max(tempMax, dp[t - 1][i] - prices[i])
    #             max_profit = max(dp[t][i], max_profit)
    #     return max_profit

    def maxProfit(self, prices):
        """
        :param prices:
        :return:
        """
        ls = len(prices)
        if ls == 0:
            return 0
        b1 = b2 = -prices[0]
        s1 = s2 = 0
        for i in range(1, ls):
            s2 = max(s2, b2 + prices[i])
            b2 = max(b2, s1 - prices[i])
            s1 = max(b1 + prices[i], s1)
            b1 = max(b1, -prices[i])
        return max(s1, s2)

