class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
        order = sorted(dic.items(), key=lambda x:x[1])
        newStr = ""
        for tup in order[::-1]:
            for i in range(tup[1]):
                newStr += tup[0]
        return newStr
