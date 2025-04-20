class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter
        c = Counter(nums)
        for i,j in c.items():
            if j>1:
                return True
        return False
        
        