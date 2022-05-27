class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def match(dic1, dic2):
            for key in dic1.keys():
                if key not in dic2 or dic1[key] != dic2[key]:
                    return False
            return True
        
        l, r = 0, len(s1)
        dic1, dic2 = Counter(s1), Counter(s2[l:r])                 
        while r < len(s2) + 1:
            if match(dic1, dic2):
                return True
            else:
                l, r = l+1, r+1
                if s2[r-1:r] in dic2:
                    dic2[s2[r-1:r]] += 1
                else:
                    dic2[s2[r-1:r]] = 1
                dic2[s2[l-1:l]] -= 1
        return False
