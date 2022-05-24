class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        count = 0
        for i in range(3): 
            for j in range(counts[i]):
                nums[count] = i
                count += 1
