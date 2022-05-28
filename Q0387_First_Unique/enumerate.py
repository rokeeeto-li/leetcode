class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = Counter(s)
        for idx, char in enumerate(s):
            if dic[char] == 1:
                return idx
        return -1
