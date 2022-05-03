#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
from collections import deque
import math


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                else:
                    mat[i][j] = math.inf

        while q:
            x, y, lvl = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if nx>=0 and ny>=0 and nx<m and ny<n and mat[nx][ny]>lvl:
                    mat[nx][ny] = lvl+1
                    q.append((nx, ny, lvl+1))

        return mat


# @lc code=end

mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
mat = [[0,1,1],[1,1,1],[1,1,1]]


so = Solution()
r = so.updateMatrix(mat)
print(r)