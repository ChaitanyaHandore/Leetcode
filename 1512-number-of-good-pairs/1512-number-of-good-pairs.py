from collections import Counter
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        d = Counter(nums)
        for key,val in d.items():
            if val>1:
                count += (val*(val-1))/2
        return count