class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sum(nums)/2
        nums=sorted(nums,reverse=True)
        r = 0
        a = []
        for i in nums:
            r+=i
            a.append(i)
            if r>s:
                break
        return a