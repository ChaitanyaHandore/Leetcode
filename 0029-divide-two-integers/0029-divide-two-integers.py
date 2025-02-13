class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Define integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        # Bitwise division using left shift
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply sign
        return -quotient if negative else quotient

# Example Usage
solution = Solution()
print(solution.divide(10, 3))  # Output: 3
print(solution.divide(7, -3))  # Output: -2
print(solution.divide(-2147483648, -1))  # Output: 2147483647
print(solution.divide(1, 1))  # Output: 1