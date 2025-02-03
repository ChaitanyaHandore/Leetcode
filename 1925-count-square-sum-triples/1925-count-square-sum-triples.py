class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ccount = 0
        for ca in range(1, n + 1):
            for cb in range(1, n + 1):
                cc = (ca ** 2 + cb ** 2) ** 0.5
                if cc.is_integer() and cc <= n:
                    ccount += 1
        return ccount

# Test cases
sol = Solution()
print(sol.countTriples(5))  # Output: 2
print(sol.countTriples(10)) # Output: 4