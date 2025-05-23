class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        r = 0
        for i in range(len(nums)):
            r = r + sum(int(cd) for cd in str(nums[i]))
        return abs(s-r)