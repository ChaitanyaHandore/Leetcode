class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"

        negative = num < 0
        num = abs(num)
        result = ""

        while num:
            result = str(num % 7) + result
            num //= 7

        return "-" + result if negative else result

# Example Usage
solution = Solution()
print(solution.convertToBase7(100))  # Output: "202"
print(solution.convertToBase7(-7))   # Output: "-10"
print(solution.convertToBase7(0))    # Output: "0"