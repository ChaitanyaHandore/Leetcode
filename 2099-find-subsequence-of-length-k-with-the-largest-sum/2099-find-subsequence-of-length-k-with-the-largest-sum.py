class Solution(object):
    def maxSubsequence(self, nums, k):
        return [n for i, n in sorted(sorted(enumerate(nums), key=lambda e: -e[1])[:k])]