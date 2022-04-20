class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        elif n == 2: return 1
        else:
            s = [0] * (n+1)
            s[1] = s[2] = 1
            for i in range(3, n+1):
                s[i] = s[i-1] + s[i-2] + s[i-3]
            return s[n]
