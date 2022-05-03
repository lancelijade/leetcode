#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque


# @lc code=start
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        q = deque()
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 10))
                elif grid[i][j] == 1:
                    cnt += 1

        if not q and cnt: return -1

        lvl = 10
        dirs = ((-1, 0), (0, 1), (0, -1), (1, 0))

        #var_dump(q)

        while q:
            x, y, lvln = q.popleft()
            if grid[x][y] < 10: 
                grid[x][y] = lvln
                lvl = lvln
            else:
                continue

            for d1, d2 in dirs:
                nx = x + d1
                ny = y + d2
                if nx>=0 and ny>=0 and nx<m and ny<n and grid[nx][ny] == 1:
                    q.append((nx, ny, lvl+10))

            #var_dump(q)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
        return lvl // 10 - 1
        
# @lc code=end


grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
grid = [[0]]
grid = [[2,2],[1,1],[0,0],[2,0]]


so = Solution()
r = so.orangesRotting(grid)
pp.pprint(r)