#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
from pprint import pprint

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


    def validPos(self, x: int, y: int) -> bool:
        return self.validRow(x) and self.validCol(y) and self.validBox(x, y)


    def place(self, x: int, y: int, n: int) -> bool:
        self.board[x][y] = str(n)
        if self.validPos(x, y): 
            return True
        else:
            return False


    def remove(self, x: int, y: int) -> None:
        self.board[x][y] = '.'


    def backtrace(self, x: int, y: int) -> bool:
        #print(x, y, self.board[0], self.board[1])
        if self.board[x][y] == ".":
            for i in range(1, 10):
                r = self.place(x, y, i)
                if r:
                    if (x, y) == (8, 8): return True
                    nx = x
                    ny = (y + 1) % 9
                    if ny == 0: nx = (x + 1) % 9
                    ne = self.backtrace(nx, ny)
                    if ne: return True
                self.remove(x, y)
        else:
            if (x, y) == (8, 8): return True
            nx = x
            ny = (y + 1) % 9
            if ny == 0: nx = (x + 1) % 9
            ne = self.backtrace(nx, ny)
            if ne: return True


    def solveSudoku(self, board: list[list[str]]) -> None:
        self.board = board
        self.backtrace(0, 0)


        
# @lc code=end

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

so = Solution()
r = so.solveSudoku(board)
pprint(board)