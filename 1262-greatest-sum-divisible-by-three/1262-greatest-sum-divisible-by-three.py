class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            prev = dp[:]
            for i in range(3):
                rem = (i + num) % 3
                dp[rem] = max(dp[rem], prev[i] + num)
        
        return dp[0]