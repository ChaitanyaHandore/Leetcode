class Solution(object):
    def integerBreak(self, n):
        if n < 4: 
            return n - 1
        r = 1
        while n > 4:
            r *= 3
            n -= 3
        return r * n