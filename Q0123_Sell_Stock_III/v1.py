class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)
        cost, sold, max_profit = float('inf'), 0, 0
        left, right = [0], [0]
        
        for i in range(N - 1):
            cost = min(cost, prices[i])
            left.append(max(left[i], prices[i+1] - cost))
            sold = max(sold, prices[N-1-i])
            right.append(max(right[i], sold - prices[N-2-i]))
            
        for i in range(N - 1):
            max_profit = max(max_profit, right[i]+left[N-i-2])
        max_profit = max(max_profit, right[-1], left[-1])
        return max_profit
