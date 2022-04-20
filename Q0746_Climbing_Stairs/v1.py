class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        cost_sum = [0] * len(cost)
        cost_sum[0] = cost[0]
        cost_sum[1] = cost[1]
        for i in range(1, len(cost)):
            cost_sum[i] = min(cost_sum[i-1]+cost[i], cost_sum[i-2]+cost[i])
        return cost_sum[-1]
