class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def checkRepeat(char = None):
            if char != None:
                if char in dic:
                    if dic[char] >= 1: 
                        return False
            for key in dic:
                if dic[key] > 1: return False
            return True
        
        def editDic(char, flag):
            if flag == 0:
                dic[char] -= 1
            if flag == 1:
                if char in dic:
                    dic[char] += 1
                else:
                    dic[char] = 1
                    
        l = r = 0
        maxLen = 0
        length = len(s)
        dic = {}
        while r < length:
            while r < length and checkRepeat(s[r]):
                editDic(s[r], 1)
                r += 1
            maxLen = max(maxLen, r-l)
            editDic(s[l], 0)
            l += 1
        return maxLen
