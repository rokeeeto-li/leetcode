class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key = lambda p:(-len(p), p))
        for word in dictionary:
            p = pw = 0
            while(p < len(s) and pw < len(word)):
                if (s[p] == word[pw]):
                    p, pw = p+1, pw+1
                else:
                    p += 1
            if pw == len(word):
               return word
        return ""
