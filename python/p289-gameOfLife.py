import pprint

pp = pprint.PrettyPrinter()
from var_dump import var_dump

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                r = self.findC(board, i, j, m, n) % 10
                #print(r)
                if board[i][j]==1:
                    if r<2: board[i][j] = 21
                    elif r>3: board[i][j] = 21
                else:
                    if r==3: board[i][j] = 10

        for i in range(m):
            for j in range(n):
                if board[i][j] > 1:
                    board[i][j] = abs(board[i][j] % 10 - 1)


    def findC(self, board, x, y, m, n) -> int:
        r = 0
        i = x - 1
        while i<=x+1 and i<m:
            j = y -1
            while j<=y+1 and j<n:
                #print(i,j)
                if i>=0 and j>=0 and [i,j]!=[x,y]:
                    r += board[i][j]
                j += 1
            i += 1
        return r


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]


so = Solution()
r = so.gameOfLife(board)
pp.pprint(board)
