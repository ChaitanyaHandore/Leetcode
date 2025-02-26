class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        maxProd = minProd = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            
            if num < 0:
                maxProd, minProd = minProd, maxProd  # Swap when encountering negative
            
            maxProd = max(num, maxProd * num)  # Max product so far
            minProd = min(num, minProd * num)  # Min product so far (for negatives)
            
            result = max(result, maxProd)  # Update global max
        
        return result