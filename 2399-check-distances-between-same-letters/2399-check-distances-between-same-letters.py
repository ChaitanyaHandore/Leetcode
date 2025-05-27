class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        seen = {}

        for i, c in enumerate(s):
            if c in seen:
                dist = i - seen[c] - 1  # distance *between* two same letters
                if dist != distance[ord(c) - ord('a')]:
                    return False
            else:
                seen[c] = i  # store first occurrence

        return True