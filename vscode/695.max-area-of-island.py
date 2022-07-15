#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dirs = ((1,0),(0,1),(0,-1),(-1,0))

        def dfs(x, y):
            #print(x, y)
            if grid[x][y] != 1:
                return 0

            grid[x][y] = 2
            s = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    s += dfs(nx, ny)
            return s

        ma = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    r = dfs(i, j)
                    ma = max(ma, r)

        return ma


        
# @lc code=end

if __name__ == "__main__":

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid = [[0,0,0,0,0,0,0,0]]

    so = Solution()
    r = so.maxAreaOfIsland(grid)
    print(r)