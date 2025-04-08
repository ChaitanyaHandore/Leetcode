class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        cnum1 = 0  # sum of numbers not divisible by m
        cnum2 = 0  # sum of numbers divisible by m
        
        for ci in range(1, n + 1):
            if ci % m == 0:
                cnum2 += ci
            else:
                cnum1 += ci
        
        return cnum1 - cnum2