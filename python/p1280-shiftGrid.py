import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        
        m = len(grid)
        n = len(grid[0])

        r = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                npos = i * n + j + k
                ni, nj = divmod(npos, n)
                if ni > m-1: ni = ni % m
                if nj > n-1: nj = nj % n
                r[ni][nj] = grid[i][j]
                #pp.pprint(r)

        return r




grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
k = 4
grid = [[1],[2],[3],[4],[7],[6],[5]]
k = 23


so = Solution()
r = so.shiftGrid(grid, k)
pp.pprint(r)