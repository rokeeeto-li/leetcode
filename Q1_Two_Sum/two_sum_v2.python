class Solution(object):
    def twoSum(self, nums, target):
        N = len(nums)
        table = {}
        for i in range(N):
            table[nums[i]] = i
        for j in range(N-1):
            if (target - nums[j] in table) and (table[target - nums[j]] != j):
                return[j, table[target - nums[j]]]
