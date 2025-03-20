class Solution(object):
    def smallestNumber(self, cn, ct):
        """
        :type cn: int
        :type ct: int
        :rtype: int
        """
        def cproduct_of_digits(cnum):
            cproduct = 1
            for cdigit in str(cnum):
                cproduct *= int(cdigit)
            return cproduct

        while True:
            if cproduct_of_digits(cn) % ct == 0:
                return cn
            cn += 1

# Test cases
sol = Solution()
print(sol.smallestNumber(10, 2))  # Output: 10
print(sol.smallestNumber(15, 3))  # Output: 16