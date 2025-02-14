class Solution(object):
    def repeatedSubstringPattern(self, cs):
        """
        :type s: str
        :rtype: bool
        """
        return cs in (cs + cs)[1:-1]