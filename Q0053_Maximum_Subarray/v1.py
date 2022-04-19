class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        current_sum = sum = nums[0]
        for i in range(1,N):
            current_sum += nums[i]
            if current_sum < nums[i]: current_sum = nums[i]
            if current_sum > sum: sum = current_sum
        return sum
