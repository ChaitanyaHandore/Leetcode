class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s = sorted(nums)
        return (s[-1] * s[-2]) - (s[0] * s[1])