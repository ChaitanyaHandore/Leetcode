class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)

        result = []
        
        # Handle negative numbers
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Convert to positive for easier handling
        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        result.append(str(numerator // denominator))
        result.append(".")

        # Fractional part
        remainder = numerator % denominator
        remainder_map = {}

        while remainder:
            # If the remainder repeats, we found a cycle
            if remainder in remainder_map:
                result.insert(remainder_map[remainder], "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator

        return "".join(result)