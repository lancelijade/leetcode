#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    
    def validRow(self, row: int) -> bool:
        v = [0] * 9
        for i in range(9):
            n = self.board[row][i]
            if n != '.':
                n = int(n) - 1
                if v[n]: return False
                v[n] = 1
        return True


    def validCol(self, col: int) -> bool:
        v = [0] * 9
        for i in range(9):
            n = self.board[i][col]
            if n != '.':
                n = int(n) - 1
                if v[n]: return False
                v[n] = 1
        return True


    def validBox(self, x: int, y: int) -> bool:
        v = [0] * 9
        x = x // 3 * 3
        y = y // 3 * 3
        for i in range(x, x+3):
            for j in range(y, y+3):
                n = self.board[i][j]
                if n != '.':
                    n = int(n) - 1
                    if v[n]: return False
                    v[n] = 1
        return True


    def isValidSudoku(self, board: list[list[str]]) -> bool:
        self.board = board

        for i in range(9):
            if not self.validRow(i): return False
            if not self.validCol(i): return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.validBox(i, j): return False

        return True

        
# @lc code=end

board = [
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

"""
board = [
 ["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
"""

so = Solution()
r = so.isValidSudoku(board)
print(r)