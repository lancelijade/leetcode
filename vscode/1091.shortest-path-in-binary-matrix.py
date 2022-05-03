#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        if grid[0][0] == 1: return -1

        n = len(grid)
        if n==1: return 1

        i = 0
        j = 0
        q = deque()
        q.append([0,0,1])

        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        while q:

            i, j, step = q.popleft()

            if grid[i][j]>0: continue
            grid[i][j] = 2

            for dir in dirs:
                ni = i + dir[0]
                nj = j + dir[1]

                if 0<=ni<n and 0<=nj<n and grid[ni][nj]==0:
                    if ni==n-1 and nj==n-1: return step+1
                    q.append([ni, nj, step+1])

        return -1
        
# @lc code=end

grid = [[0,1],[1,0]]
grid = [[0,0,0],[1,1,0],[1,1,0]]
#grid = [[1,0,0],[1,1,0],[1,1,0]]
#grid = [[0]]

so = Solution()
r = so.shortestPathBinaryMatrix(grid)
pp.pprint(r)