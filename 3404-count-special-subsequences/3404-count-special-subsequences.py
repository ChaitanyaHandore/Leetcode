class Solution(object):
    def numberOfSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        ct = Counter()
        for q in range(2, len(nums) - 4):
            for p in range(q - 1):
                ct[nums[p] * 1.0 / nums[q]] += 1
            r = q + 2
            for s in range(r + 2, len(nums)):
                ans += ct[nums[s] * 1.0 / nums[r]]
        return ans