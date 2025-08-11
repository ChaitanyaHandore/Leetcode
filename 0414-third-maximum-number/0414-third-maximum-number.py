class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(set(nums), reverse=True)  # sort descending
        return n[2] if len(n) >= 3 else n[0]