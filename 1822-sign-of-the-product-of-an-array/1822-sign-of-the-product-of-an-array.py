class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        csign = 1
        for cnum in nums:
            if cnum == 0:
                return 0
            elif cnum < 0:
                csign *= -1
        return csign