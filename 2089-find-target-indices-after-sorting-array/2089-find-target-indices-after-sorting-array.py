class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = []
        nums = sorted(nums)
        for i,j in enumerate(nums):
            if j==target:
                a.append(i)

        return a