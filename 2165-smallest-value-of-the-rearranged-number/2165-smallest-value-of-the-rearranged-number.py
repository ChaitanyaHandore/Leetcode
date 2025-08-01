class Solution(object):
    def smallestNumber(self, a):
        """
        :type num: int
        :rtype: int
        """
        s = sorted(str(abs(a)))
        if a <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))
