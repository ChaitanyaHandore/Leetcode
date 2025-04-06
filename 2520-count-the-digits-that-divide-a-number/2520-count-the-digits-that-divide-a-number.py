class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum(1 if num % int(d) == 0 else 0 for d in str(num))