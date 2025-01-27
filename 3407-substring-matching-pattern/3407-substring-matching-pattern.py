class Solution(object):
    def hasMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(c_s, c_p):
            # Base cases
            if not c_p:  # If pattern is empty
                return not c_s  # True only if the string is also empty
            if not c_s and c_p == '*':  # Handle patterns like "*"
                return True
            
            # Check first character match or if pattern is '*'
            first_match = bool(c_s) and (c_p[0] in {c_s[0], '?'})
            
            if c_p[0] == '*':
                # '*' can match zero characters (move pattern) or match one character (move string)
                return match(c_s, c_p[1:]) or (bool(c_s) and match(c_s[1:], c_p))
            else:
                # Move to the next character in both string and pattern
                return first_match and match(c_s[1:], c_p[1:])
        
        return match(s, p)

# Test
solution = Solution()
s = "leetcode"
p = "ee*e"
print(solution.hasMatch(s, p))  # Output: True