class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, current, right = 0, 0, len(nums) - 1
        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left, current = left + 1, current + 1
            elif nums[current] == 1:
                current = current + 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
