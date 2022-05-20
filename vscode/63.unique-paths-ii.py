#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from collections import deque
from functools import cache

class Solution:
    # brute force
    def uniquePathsWithObstacles_bf(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0
        q = deque()
        q.append((-1, 0))
        r = 0

        while q:
            x, y = q.popleft()
            for nx, ny in [[x, y+1], [x+1, y]]:
                if (nx, ny) == (m-1, n-1):
                    r += 1
                    continue

                if 0<=nx<m and 0<=ny<n and obstacleGrid[nx][ny]==0:
                    q.append((nx, ny))
        return r


    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1: return 0

        @cache
        def bfs(x: int, y: int) -> int:
            if (x, y) == (m-1, n-1):
                return 1
            if x>=m or y>=n or obstacleGrid[x][y] == 1:
                return 0
            return bfs(x+1, y) + bfs(x, y+1)

        return bfs(0, 0)

        
# @lc code=end

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[0,0],[0,1]]
obstacleGrid = [[0]]
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [
    [0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],
    [1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
    [0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
    [0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],
    [0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],
    [1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],
    [1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]



so = Solution()
r = so.uniquePathsWithObstacles(obstacleGrid)
print(r)