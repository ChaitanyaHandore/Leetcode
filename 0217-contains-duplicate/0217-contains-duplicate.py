class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        c = Counter(nums)
        for i,j in c.items():
            if j >1:
                return True
        return False