from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        m1 = max(nums)
        m2 = min(nums)
        for x in nums:
            if x != m1 and x != m2:
                return x
        return -1