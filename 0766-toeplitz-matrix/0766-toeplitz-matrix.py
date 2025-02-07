class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        cRows, cCols = len(matrix), len(matrix[0])
        
        for cRow in range(cRows - 1):
            for cCol in range(cCols - 1):
                if matrix[cRow][cCol] != matrix[cRow + 1][cCol + 1]:
                    return False
        return True