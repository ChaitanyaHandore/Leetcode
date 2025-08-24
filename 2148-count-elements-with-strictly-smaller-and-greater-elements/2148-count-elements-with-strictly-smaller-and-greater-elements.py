class Solution:
    def countElements(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        return len(nums) - nums.count(max(nums)) - nums.count(min(nums))