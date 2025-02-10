class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmax_num = max(nums)
        cmax_index = nums.index(cmax_num)

        for cnum in nums:
            if cnum != cmax_num and cmax_num < 2 * cnum:
                return -1
        
        return cmax_index