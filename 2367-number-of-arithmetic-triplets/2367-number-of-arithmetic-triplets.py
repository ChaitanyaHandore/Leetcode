class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        counter = 0
        numSet = set(nums) 
        for num in nums:
            if (num + diff) in numSet and (num + 2 * diff) in numSet:
                counter += 1
        
        return counter