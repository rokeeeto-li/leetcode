class Solution(object):
    def getSum(self, a, b):
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1
        
        if a*b >= 0:
            while (y != 0):
                sum = x ^ y
                carry = x & y
                x = sum
                y = carry << 1
        else:
            while (y != 0):
                sum = x ^ y
                borrow = (~x) & y
                x = sum
                y = borrow << 1
        return x * sign
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
