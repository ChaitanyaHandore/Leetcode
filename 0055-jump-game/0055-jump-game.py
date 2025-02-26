class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxReach = 0  # The farthest index that can be reached
        n = len(nums)

        for i in range(n):
            if i > maxReach:  # If current index is beyond maxReach, we are stuck
                return False
            maxReach = max(maxReach, i + nums[i])  # Update the farthest reachable index
            if maxReach >= n - 1:  # If we can reach or exceed the last index, return True
                return True
        
        return False