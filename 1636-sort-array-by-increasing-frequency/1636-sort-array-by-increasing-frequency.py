from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        cfreq = Counter(nums)
        
        # Sort by frequency (ascending) and then by value (descending)
        return sorted(nums, key=lambda cnum: (cfreq[cnum], -cnum))