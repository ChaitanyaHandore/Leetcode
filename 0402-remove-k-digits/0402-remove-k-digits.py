class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        c_stack = []
        
        for c_digit in num:
            while c_stack and k > 0 and c_stack[-1] > c_digit:
                c_stack.pop()
                k -= 1
            c_stack.append(c_digit)
        
        # Remove remaining k digits from the end if needed
        c_stack = c_stack[:-k] if k else c_stack
        
        # Convert to string and remove leading zeros
        c_result = "".join(c_stack).lstrip('0')
        
        return c_result if c_result else "0"

# Test cases
sol = Solution()
print(sol.removeKdigits("1432219", 3))  # Output: "1219"
print(sol.removeKdigits("10200", 1))    # Output: "200"
print(sol.removeKdigits("10", 2))       # Output: "0"