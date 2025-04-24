class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        clen = len(nums)
        coutput = [1] * clen
        
        # First pass: left product
        cleft_product = 1
        for i in range(clen):
            coutput[i] = cleft_product
            cleft_product *= nums[i]
        
        # Second pass: right product
        cright_product = 1
        for i in range(clen - 1, -1, -1):
            coutput[i] *= cright_product
            cright_product *= nums[i]
        
        return coutput