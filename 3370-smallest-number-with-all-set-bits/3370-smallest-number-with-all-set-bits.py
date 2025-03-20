class Solution(object):
    def smallestNumber(self, cn):
        """
        :type cn: int
        :rtype: int
        """
        cbit_length = cn.bit_length()  # Get the number of bits required
        return (1 << cbit_length) - 1  # Create a number with all bits set

# Test cases
sol = Solution()
print(sol.smallestNumber(5))   # Output: 7
print(sol.smallestNumber(10))  # Output: 15
print(sol.smallestNumber(3))   # Output: 3