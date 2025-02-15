class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def processString(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        return processString(s) == processString(t)

# Example usage:
sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))  # Output: True
print(sol.backspaceCompare("ab##", "c#d#"))  # Output: True
print(sol.backspaceCompare("a#c", "b"))      # Output: False