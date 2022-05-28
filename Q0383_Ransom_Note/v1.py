class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic1 = Counter(ransomNote)
        dic2 = Counter(magazine)
        for key in dic1.keys():
            if key not in dic2 or dic2[key] < dic1[key]:
                return False
        return True
