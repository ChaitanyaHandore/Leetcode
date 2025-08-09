class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter(nums)
        r, f = c.most_common(1)[0]
        return r