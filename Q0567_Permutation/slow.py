class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def matchStr(str1, str2):
            dic1 = {}
            dic2 = {}
            for char in str1:
                if char not in dic1:
                    dic1[char] = 1
                else:
                    dic1[char] += 1
            for char in str2:
                if char not in dic2:
                    dic2[char] = 1
                else:
                    dic2[char] += 1
            if dic1 == dic2:
                return True
            return False          

        l, r = 0, len(s1)
        while r < len(s2) + 1:
            if matchStr(s1, s2[l:r]):
                return True
            else:
                l, r = l+1, r+1
        return False
