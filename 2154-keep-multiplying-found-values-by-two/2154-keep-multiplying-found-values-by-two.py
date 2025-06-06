class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        cmap = {num: True for num in nums}
        while True:
            if original in cmap:
                original*=2
            else:
                break
        return original
                