class Solution(object):
    def maxProduct(self, n):
        digs = []
        while n > 0:
            digs.append(n % 10)
            n //= 10
        digs.sort()
        return digs[-1] * digs[-2]