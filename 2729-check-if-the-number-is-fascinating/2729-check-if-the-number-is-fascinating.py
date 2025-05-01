class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c1 = 2 * n
        c2 = 3 * n
        c = str(n) + str(c1) + str(c2)
        
        # Check length is exactly 9 and all digits from 1 to 9 appear once
        return len(c) == 9 and set(c) == set("123456789")