class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        c_stack = []  # Stack to store characters

        for c_char in s:
            if c_char.isdigit():
                if c_stack:
                    c_stack.pop()  # Remove closest non-digit character
            else:
                c_stack.append(c_char)  # Push letters onto the stack

        return ''.join(c_stack)  # Final string after removals