class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0;
        nums1_copy = nums1[:m] 
        while p1 < m and p2 < n:
            if nums1_copy[p1] <= nums2[p2]:
                nums1[p1+p2] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p1+p2] = nums2[p2]
                p2 += 1
                
        if p1 < m: 
            nums1[p1+p2: n+m] = nums1_copy[p1:m]
        if p2 < n: 
            nums1[p1+p2: n+m] = nums2[p2:n]
