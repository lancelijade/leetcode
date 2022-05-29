#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
import math

class Solution:

    def placeQueen(self, x, y):
        #print(x, y, self.matrix)
        if self.matrix[x][y] == 0:
            self.matrix[x][y] = math.inf
            for i in range(self.n):
                self.matrix[i][y] += 1
                self.matrix[x][i] += 1
                for dx, dy in [[x+i, y+i], [x-i, y-i], [x+i, y-i], [x-i, y+i]]:
                    if 0<=dx<self.n and 0<=dy<self.n: self.matrix[dx][dy] += 1
            return True
        else:
            return False

    def removeQueen(self, x, y):
        self.matrix[x][y] = 0
        for i in range(self.n):
            if self.matrix[i][y]>0: self.matrix[i][y] -= 1
            if self.matrix[x][i]>0: self.matrix[x][i] -= 1
            for dx, dy in [[x+i, y+i], [x-i, y-i], [x+i, y-i], [x-i, y+i]]:
                if 0<=dx<self.n and 0<=dy<self.n and self.matrix[dx][dy]>0: self.matrix[dx][dy] -= 1

    def backtrackPlace(self, x, count):
        for y in range(self.n):
            r = self.placeQueen(x, y)
            if r:
                count += 1
                if count == self.n:
                    #print("RESULT:", self.matrix)
                    self.recordResult()
                else:
                    self.backtrackPlace(x+1, count)
                count -= 1
                self.removeQueen(x, y)

    def recordResult(self):
        t = [['.'] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == math.inf:
                    t[i][j] = 'Q'
            t[i] = ''.join(t[i])
        self.r.append(t)
    

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.r = []
        self.matrix = [[0] * n for _ in range(n)]
        self.n = n

        self.backtrackPlace(0, 0)

        return self.r

        
# @lc code=end

n = 4
n = 1

so = Solution()
r = so.solveNQueens(n)
print(r)