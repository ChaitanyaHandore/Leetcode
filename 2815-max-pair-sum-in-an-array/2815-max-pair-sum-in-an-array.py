class Solution(object):
    def maxSum(self, nums):
        maximum = -1
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if max(str(nums[i])) == max(str(nums[j])):
                    if nums[i] + nums[j] > maximum:
                        maximum = nums[i] + nums[j] 
        return maximum