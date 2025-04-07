class Solution:
    def alternateDigitSum(self, n) :
        num = str(n)
        result, factor = 0, 1
        for c in num:
            result += int(c) * factor
            factor *= -1
        return result