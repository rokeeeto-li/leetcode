class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 0
        order = sorted(dic.items(), key=lambda x:x[1])
        value = []
        for i in range(k):
            value.append(order[-i-1][0])
        return value
