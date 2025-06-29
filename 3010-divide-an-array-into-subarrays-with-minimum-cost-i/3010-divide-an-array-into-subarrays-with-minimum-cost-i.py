class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cmin_cost = float('inf')
        clen = len(nums)
        
        for ci in range(1, clen - 1):
            for cj in range(ci + 1, clen):
                ccost = nums[0] + nums[ci] + nums[cj]
                cmin_cost = min(cmin_cost, ccost)
        
        return cmin_cost