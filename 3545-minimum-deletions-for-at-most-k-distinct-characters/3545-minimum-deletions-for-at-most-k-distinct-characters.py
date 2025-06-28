from collections import Counter

class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        delet = 0
        count = Counter(s)  # Automatically creates a dictionary with character counts

        if len(count) < k:
            return 0

        freq = sorted(count.values())

        while len(freq) > k:
            delet += freq.pop(0)

        return delet