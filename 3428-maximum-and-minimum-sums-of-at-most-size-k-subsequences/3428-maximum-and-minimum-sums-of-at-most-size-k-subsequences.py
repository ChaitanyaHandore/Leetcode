class Solution:
    MOD = 10 ** 9 + 7
    def minMaxSums(self, nums, k):
        nums.sort()
        n = len(nums)
        total = 0
        
        # Pre-calculate combinations table
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # Base cases
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, min(i + 1, k + 1)):
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % self.MOD
        
        # Calculate sum using pre-computed combinations
        for i in range(n):
            for j in range(1, k + 1):
                total = (total + nums[i] * dp[i][j-1]) % self.MOD
                total = (total + nums[i] * dp[n-i-1][j-1]) % self.MOD
                
        return total
                

            