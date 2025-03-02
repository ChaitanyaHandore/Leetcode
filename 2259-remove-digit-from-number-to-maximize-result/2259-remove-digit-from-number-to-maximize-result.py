class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        cmax_result = ""
        
        for ci in range(len(number)):
            if number[ci] == digit:
                cnew_number = number[:ci] + number[ci+1:]
                cmax_result = max(cmax_result, cnew_number)
        
        return cmax_result

# Test cases
sol = Solution()
print(sol.removeDigit("123", "3"))   # Output: "12"
print(sol.removeDigit("1231", "1"))  # Output: "231"
print(sol.removeDigit("551", "5"))   # Output: "51"