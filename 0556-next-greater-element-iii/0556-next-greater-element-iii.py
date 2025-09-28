class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))   # convert number to list of chars
        i = len(digits) - 2

        # Step 1: Find pivot (first decreasing digit from right)
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1

        if i == -1:   # digits are in descending order → no greater permutation
            return -1

        # Step 2: Find successor (smallest digit larger than pivot, from right side)
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3: Swap pivot and successor
        digits[i], digits[j] = digits[j], digits[i]

        # Step 4: Reverse the suffix (i+1 → end)
        digits[i+1:] = reversed(digits[i+1:])

        # Convert back to integer
        result = int("".join(digits))

        # Step 5: Check 32-bit signed integer limit
        return result if result <= 2**31 - 1 else -1