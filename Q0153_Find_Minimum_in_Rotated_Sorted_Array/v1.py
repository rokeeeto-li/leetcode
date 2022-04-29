class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1 or nums[-1] > nums[0]): return nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)//2
            if nums[mid] > nums[mid+1]: return nums[mid+1]
            if nums[mid] > nums[0]: l = mid + 1
            else: r = mid
        return nums[l]
