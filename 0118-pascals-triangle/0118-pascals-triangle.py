class Solution(object):
    def generate(self, cNumRows):
        """
        :type cNumRows: int
        :rtype: List[List[int]]
        """
        cTriangle = []
        
        for cRow in range(cNumRows):
            cNewRow = [1] * (cRow + 1)  # Create a row with all elements as 1
            for cCol in range(1, cRow):  # Update inner elements
                cNewRow[cCol] = cTriangle[cRow - 1][cCol - 1] + cTriangle[cRow - 1][cCol]
            cTriangle.append(cNewRow)
        
        return cTriangle

# Example usage:
solution = Solution()
numRows = 5
print(solution.generate(numRows))