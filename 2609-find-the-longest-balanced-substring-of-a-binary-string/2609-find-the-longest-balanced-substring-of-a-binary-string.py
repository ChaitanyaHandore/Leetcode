class Solution(object):
    def findTheLongestBalancedSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cMaxLength = 0
        cZeroCount = cOneCount = 0

        for c in s:
            if c == '0':
                if cOneCount > 0:  # Reset when encountering a new sequence
                    cZeroCount = 0
                    cOneCount = 0
                cZeroCount += 1
            else:  # c == '1'
                cOneCount += 1
                cMaxLength = max(cMaxLength, min(cZeroCount, cOneCount) * 2)

        return cMaxLength

# Test cases
sol = Solution()
print(sol.findTheLongestBalancedSubstring("01000111"))  # Output: 6
print(sol.findTheLongestBalancedSubstring("00111"))     # Output: 4
print(sol.findTheLongestBalancedSubstring("111"))       # Output: 0