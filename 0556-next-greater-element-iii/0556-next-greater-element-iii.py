class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        cDigits = list(str(n))  # Convert number to list of digits
        cLen = len(cDigits)

        # Step 1: Find the first decreasing element from the right
        cI = cLen - 2
        while cI >= 0 and cDigits[cI] >= cDigits[cI + 1]:
            cI -= 1

        # If no such element is found, return -1 (already the largest permutation)
        if cI == -1:
            return -1

        # Step 2: Find the smallest number greater than cDigits[cI] on its right
        cJ = cLen - 1
        while cDigits[cJ] <= cDigits[cI]:
            cJ -= 1

        # Step 3: Swap them
        cDigits[cI], cDigits[cJ] = cDigits[cJ], cDigits[cI]

        # Step 4: Reverse the part after index cI
        cDigits[cI + 1:] = reversed(cDigits[cI + 1:])

        # Convert back to integer
        cResult = int("".join(cDigits))

        # Check if result fits in 32-bit integer
        return cResult if cResult < 2**31 else -1