from collections import Counter

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # If typed is shorter than name, it's immediately invalid
        if len(typed) < len(name):
            return False

        # Count character frequencies
        c1 = Counter(name)
        c2 = Counter(typed)

        # If typed has fewer occurrences of any character, return False
        for c in c1:
            if c2[c] < c1[c]:
                return False

        # Check character order
        cname, ctyped = 0, 0
        while ctyped < len(typed):
            if cname < len(name) and name[cname] == typed[ctyped]:
                cname += 1
            elif ctyped == 0 or typed[ctyped] != typed[ctyped - 1]:
                return False
            ctyped += 1

        return cname == len(name)