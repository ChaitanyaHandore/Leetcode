from collections import Counter
from fractions import gcd  # Use fractions module in Python 2
from functools import reduce

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck:
            return False
        
        count = Counter(deck)
        freq_values = list(count.values())

        # Find the GCD of all frequency values
        gcd_value = reduce(gcd, freq_values)
        
        return gcd_value > 1

# Example test cases
solution = Solution()
print(solution.hasGroupsSizeX([1,2,3,4,4,3,2,1]))  # Output: True
print(solution.hasGroupsSizeX([1,1,1,2,2,2,3,3]))  # Output: False