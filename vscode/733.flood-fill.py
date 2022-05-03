#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from collections import deque


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        cl = image[sr][sc]
        if cl == newColor: return image 

        m, n = len(image), len(image[0])
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        image[sr][sc] = newColor
        q = deque()
        q.append((sr, sc))

        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if nx>=0 and ny>=0 and nx<m and ny<n and image[nx][ny] == cl:
                    image[nx][ny] = newColor
                    q.append((nx, ny))

        return image

        
# @lc code=end

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2

image = [[0,0,0],[0,1,0]]
sr = 1
sc = 1
newColor = 2

image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1

so = Solution()
r = so.floodFill(image, sr, sc, newColor)
print(r)