class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True  # Already equal
        
        # Find indices where characters differ
        c_diffs = [(c_x, c_y) for c_x, c_y in zip(s1, s2) if c_x != c_y]
        
        # Must have exactly two differences and swapping them should match
        return len(c_diffs) == 2 and c_diffs[0] == c_diffs[1][::-1]