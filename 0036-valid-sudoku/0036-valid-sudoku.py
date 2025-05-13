class Solution(object):
    def isValidSudoku(self, board):
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    row_val = ("row", r, board[r][c])
                    col_val = ("col", c, board[r][c])
                    grid_val = ("grid", r // 3, c // 3, board[r][c])

                    if row_val in seen or col_val in seen or grid_val in seen:
                        return False
                    else:
                        seen.add(row_val)
                        seen.add(col_val)
                        seen.add(grid_val)
        
        return True