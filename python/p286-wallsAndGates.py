from collections import deque
from var_dump import var_dump
import pprint
pp = pprint.PrettyPrinter()
from datetime import datetime 
time_start = datetime.now()

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        q = deque()
        INF = 2147483647
        m = len(rooms)
        n = len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: q.append((i, j, 0))

        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        while q:
            x, y, step = q.popleft()
            if rooms[x][y] != INF and rooms[x][y] != 0: continue

            rooms[x][y] = step

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if nx>=0 and ny>=0 and nx<m and ny<n and rooms[nx][ny] == INF:
                    q.append((nx, ny, step+1))

            #print(q)


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

so = Solution()
so.wallsAndGates(rooms)
print(rooms)