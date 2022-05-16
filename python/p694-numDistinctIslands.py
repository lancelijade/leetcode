from collections import deque

class Solution:

    def numDistinctIslands(self, grid: list[list[int]]) -> int:

        # bfs to find island, return the list of point in island
        def bfs(grid: list[list[int]]) -> list[tuple]:
            dirs = ((-1,0),(1,0),(0,-1),(0,1))
            li = []
            while q:
                x, y = q.popleft()
                if (x, y) not in li:
                    grid[x][y] = 2
                    li.append((x, y))
                    for dx, dy in dirs:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]==1:
                            q.append((nx, ny))
            return li
            

        # modify the island point list relative
        def normalize(ld: list[tuple]) -> list[tuple]:
            ld.sort()
            x0, y0 = ld[0]
            ld[0] = (0, 0)
            for i in range(1, len(ld)):
                ld[i] = (ld[i][0]-x0, ld[i][1]-y0)
            return tuple(ld)


        m, n = len(grid), len(grid[0])
        unique = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q = deque()
                    q.append((i,j))
                    r = bfs(grid)
                    #print(r)
                    unique.add(normalize(r))

        #print(unique)
        return len(unique)


def log(func):
    def wrapper(*args, **kw):
        from datetime import datetime 
        time_start = datetime.now()
        #print('call %s():' % func.__name__)
        r = func(*args, **kw)
        time_end = datetime.now()
        print("---\ntime cost:",time_end-time_start)
        return r
    return wrapper

@log
def run(*args, **kw):
    so = Solution()
    r = so.numDistinctIslands(*args, **kw)
    print(r)

grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
#grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
run(grid)