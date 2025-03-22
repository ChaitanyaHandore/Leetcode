class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sum(n if n < 10 else -n for n in nums) != 0