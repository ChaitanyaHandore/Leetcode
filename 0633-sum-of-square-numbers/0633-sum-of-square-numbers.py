import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        cA, cB = 0, int(math.sqrt(c))  # Start with two pointers
        
        while cA <= cB:
            cSum = cA * cA + cB * cB
            if cSum == c:
                return True
            elif cSum < c:
                cA += 1  # Increase left pointer
            else:
                cB -= 1  # Decrease right pointer
        
        return False  # No valid pair found