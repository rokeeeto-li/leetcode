class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        pos = []
        while (l < r):
            mid = (l+r)//2
            if (nums[mid] >= target): r = mid
            else: l = mid + 1
        pos.append(l)
        l, r = pos[0], len(nums) - 1
        while (l < r):
            mid = (l+r+1)//2
            if (nums[mid] > target): r = mid - 1
            else: l = mid
        pos.append(l)
        return pos
