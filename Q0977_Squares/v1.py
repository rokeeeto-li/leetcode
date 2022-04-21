class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        left = 0
        right = n - 1
        result  = [0]*n
        for i in range(n - 1, -1, -1):
            if(abs(nums[left]) <= abs(nums[right])):
                result[i] = nums[right]*nums[right]
                right -= 1
            else:
                result[i] = nums[left]*nums[left]
                left += 1
        return result
