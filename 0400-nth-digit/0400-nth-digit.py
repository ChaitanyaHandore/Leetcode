class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Determine which range the nth digit falls into
        length = 1  # Length of the current number group (1-digit, 2-digit, etc.)
        count = 9    # Count of numbers in the current group (9 numbers in the 1-digit group, 90 numbers in the 2-digit group, etc.)
        start = 1    # The first number in the current group (1 for 1-digit, 10 for 2-digit, etc.)
        
        # Find the range where the nth digit is located
        while n > length * count:
            n -= length * count  # Reduce n by the number of digits in the current group
            length += 1           # Move to the next length of numbers (2-digit, 3-digit, etc.)
            count *= 10           # Increase count (10, 100, 1000...)
            start *= 10           # Move to the next group of numbers (10, 100, 1000...)
        
        # Determine the actual number that contains the nth digit
        num = start + (n - 1) // length  # Find the exact number
        digit_index = (n - 1) % length   # Find the exact digit index within the number
        
        # Convert the number to a string and return the digit at the digit_index
        return int(str(num)[digit_index])

# Example test cases
solution = Solution()
print(solution.findNthDigit(3))  # Output: 3
print(solution.findNthDigit(11)) # Output: 0