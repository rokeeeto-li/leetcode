class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        pg = ps = 0
        m = len(g)
        n = len(s)
        num = 0
        g.sort()
        s.sort()
        while pg < m and ps < n:
            if (g[pg] <= s[ps]):
                pg += 1
                ps += 1
                num += 1
            else: ps += 1
        return num
