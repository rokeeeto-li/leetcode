class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = max_length = 0
        n = len(s)
        dic = {}
        while r < n:
            dic[s[r]] = r
            r += 1
            
            if len(dic) == 3:
                delete_index = min(dic.values())
                del dic[s[delete_index]]
                l = delete_index + 1
            
            max_length = max(max_length, r - l)
        return max_length
