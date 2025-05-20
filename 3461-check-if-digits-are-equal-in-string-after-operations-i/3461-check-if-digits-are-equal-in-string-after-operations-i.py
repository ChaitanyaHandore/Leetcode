class Solution(object):
    def hasSameDigits(self, s):
        while len(s) > 2:
            newborn_string = ""
            for i in range(len(s) - 1):
                first_digit = int(s[i])               # Convert char to int
                second_digit = int(s[i + 1])          # Convert char to int
                new_digit = (first_digit + second_digit) % 10  # Calculate new digit
                newborn_string += str(new_digit)      # Append new digit to the new string
            s = newborn_string                        # Update s to the new string
        # Check if the final two digits are the same
        return s[0] == s[1]