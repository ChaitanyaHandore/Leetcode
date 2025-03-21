class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        c_count = 0
        c_m = min(a, b)
        
        for c_i in range(1, c_m + 1):  # Start from 1 to avoid division by zero
            if a % c_i == 0 and b % c_i == 0:
                c_count += 1
                
        return c_count