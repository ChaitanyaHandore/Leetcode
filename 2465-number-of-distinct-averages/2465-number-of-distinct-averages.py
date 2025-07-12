class Solution:
    def distinctAverages(self, nums):
        if len(nums) <= 1:
            return 0
        nums.sort()  # Sort the array
        unique_avg = set()

        left, right = 0, len(nums) - 1

        while left < right:
            avg = (nums[left] + nums[right]) / 2.0
            unique_avg.add(avg)
            left += 1
            right -= 1

        return len(unique_avg)