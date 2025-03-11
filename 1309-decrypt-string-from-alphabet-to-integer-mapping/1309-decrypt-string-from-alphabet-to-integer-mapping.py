class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        cresult = []
        ci = len(s) - 1
        
        while ci >= 0:
            if s[ci] == '#':  # If '#' is found, process two-digit mapping
                cnum = int(s[ci - 2:ci])  # Extract the two-digit number
                cresult.append(chr(96 + cnum))  # Convert to corresponding letter
                ci -= 3  # Move back by 3 positions
            else:
                cnum = int(s[ci])  # Extract single digit
                cresult.append(chr(96 + cnum))  # Convert to letter
                ci -= 1  # Move back by 1 position
                
        return ''.join(reversed(cresult))  # Reverse result as we processed from right to left

# **Test Cases**
solution = Solution()
print(solution.freqAlphabets("10#11#12"))  # Output: "jkab"
print(solution.freqAlphabets("1326#"))     # Output: "acz"