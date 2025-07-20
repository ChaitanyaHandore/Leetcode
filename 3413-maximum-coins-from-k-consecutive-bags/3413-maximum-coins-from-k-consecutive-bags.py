class Solution(object):
    def maximumCoins(self, coins, k):
        """
        :type coins: List[List[int]]
        :type k: int
        :rtype: int
        """
        coins.sort()
        n = len(coins)

        curr_sum = 0
        ans = 0

        # Case 1: Forward partial
        j = 0
        for i in range(n):
            while j < n and coins[j][1] <= coins[i][0] + k - 1:
                curr_sum += (coins[j][1] - coins[j][0] + 1) * coins[j][2]
                j += 1

            if j < n:
                partial = max(0, (coins[i][0] + k - 1 - coins[j][0] + 1) * coins[j][2])
                ans = max(ans, curr_sum + partial)

            curr_sum -= (coins[i][1] - coins[i][0] + 1) * coins[i][2]

        # Case 2: Back partial sum
        curr_sum = 0
        j = 0
        for i in range(n):
            curr_sum += (coins[i][1] - coins[i][0] + 1) * coins[i][2]

            while coins[j][1] < coins[i][1] - k + 1:
                curr_sum -= (coins[j][1] - coins[j][0] + 1) * coins[j][2]
                j += 1

            partial = max(0, ((coins[i][1] - k + 1) - coins[j][0]) * coins[j][2])
            ans = max(ans, curr_sum - partial)

        return ans



