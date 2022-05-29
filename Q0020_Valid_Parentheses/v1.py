class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in ['(','{','[']:
                left.append(char)
            else:
                if left == [] or mapping[char] != left[-1]:
                    return False
                else:
                    left.pop()
        if left != []: return False
        return True
