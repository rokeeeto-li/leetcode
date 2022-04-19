class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_min, profit = float('inf'), 0
        for i in range(len(prices)):
            if current_min > prices[i]: current_min = prices[i]
            elif profit < prices[i]- current_min: profit = prices[i]- current_min
        return profit
