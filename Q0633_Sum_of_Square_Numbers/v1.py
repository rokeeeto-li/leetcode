class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(sqrt(c))
        for i in range(0, n+1, 1):
            l, r = i, n
            while (l <= r):
                mid = (l+r)//2
                if mid*mid + i*i == c:
                    return True
                elif mid*mid + i*i > c:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
