class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        map = {}
        inter_num = []
        for num in nums1:
            if num in map: map[num] += 1
            else: map[num] = 1
        
        for num in nums2:
            if num in map:
                if map[num] > 0: 
                    map[num] -= 1
                    inter_num.append(num)
        return inter_num
