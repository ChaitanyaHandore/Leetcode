from collections import Counter

class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        ccount = Counter(s)

        for i in range(len(s) - 1):
            c1, c2 = s[i], s[i + 1]
            
            if c1 != c2:
                # Check frequency condition
                if ccount[c1] == int(c1) and ccount[c2] == int(c2):
                    return c1 + c2

        return ""