class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        
        # Base case: the first two steps
        prev1 = cost[0]
        prev2 = cost[1]
        
        # Start iterating from the 2nd step (index 2) to the last step
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev1 = prev2
            prev2 = current
        
        # The minimum cost to reach the top is the minimum of the last two steps
        return min(prev1, prev2)