class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums,reverse=True)
        return (s[0]-1)*(s[1]-1)