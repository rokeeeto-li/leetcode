class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        current_min, profit = float('inf'), 0
        for i in range(len(prices)):
            current_min = min(current_min, prices[i])
            profit = max(profit, prices[i]- current_min)
        return profit
