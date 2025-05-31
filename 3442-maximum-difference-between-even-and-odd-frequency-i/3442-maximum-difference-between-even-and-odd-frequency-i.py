from sys import maxsize
from collections import Counter

class Solution:
    def maxDifference(self, string):
        max_odd = -maxsize
        min_even = maxsize

        for freq in Counter(string).values():
            if freq & 1:  # odd frequency
                max_odd = max(max_odd, freq)
            else:  # even frequency
                min_even = min(min_even, freq)

        return max_odd - min_even