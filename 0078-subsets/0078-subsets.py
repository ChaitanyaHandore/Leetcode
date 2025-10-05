class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from itertools import combinations
        subsets= []
        for i in range(len(nums)+1):
            for combo in combinations(nums,i):
                subsets.append(list(combo))
        return subsets