class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i < m - 1 and grid[i][j] != grid[i + 1][j]:
                    return False
                if j < n - 1 and grid[i][j] == grid[i][j + 1]:
                    return False
        
        return True