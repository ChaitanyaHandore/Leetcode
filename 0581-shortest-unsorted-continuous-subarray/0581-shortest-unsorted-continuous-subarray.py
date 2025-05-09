class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sorted(nums)
        if s == nums:
            return 0
        
        left = 0
        while left < len(nums) and nums[left] == s[left]:
            left += 1

        right = len(nums) - 1
        while right > left and nums[right] == s[right]:
            right -= 1

        return right - left + 1