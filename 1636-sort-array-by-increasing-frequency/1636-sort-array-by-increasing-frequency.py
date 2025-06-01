from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ccount = Counter(nums)
        # Sort by frequency increasing, and value decreasing for ties
        csorted = sorted(nums, key=lambda cx: (ccount[cx], -cx))
        return csorted