class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append((s1[i], s2[i]))
        
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]