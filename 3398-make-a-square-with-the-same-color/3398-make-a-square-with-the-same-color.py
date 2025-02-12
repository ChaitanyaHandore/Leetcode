class Solution:
    def canMakeSquare(self, grid):

        for i,j in product([0,1],[0,1]):
            square =(grid[i  ][j  ] + grid[i  ][j+1] +
                     grid[i+1][j  ] + grid[i+1][j+1])

            if countOf(square, "B") != 2: return True
            
        return False