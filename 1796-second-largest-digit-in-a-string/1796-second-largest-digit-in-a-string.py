class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        cdigits_set = set(int(c) for c in s if c.isdigit())
        if len(cdigits_set) < 2:
            return -1
        cdigits_sorted = sorted(cdigits_set, reverse=True)
        return cdigits_sorted[1]