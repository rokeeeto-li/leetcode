class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        start = 0
        end = len(arr) - 1
        while (start < end):
            mid = (start+end) >> 1
            if arr[mid] > arr[mid+1]: end = mid
            else: start = mid + 1
        return start
