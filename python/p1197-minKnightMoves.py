from collections import deque
import math
#from pprint import pprint

class Solution:

    def minKnightMoves(self, x: int, y: int) -> int:

        xmi, xma = (x, 0) if x <= 0 else (0, x)
        ymi, yma = (y, 0) if y <= 0 else (0, y)

        m = self.fill(xmi-2, xma+2, ymi-2, yma+2)

        return m[x][y]


    def fill(self, xmi, xma, ymi, yma) -> list[list[int]]:
        m = {}
        for i in range(xmi, xma+1):
            m[i] = {}
            for j in range(ymi, yma+1):
                m[i][j] = math.inf
        m[0][0] = 0

        dirs = ((2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))

        q = deque([(0, 0, 0)])
        while q:
            x, y, lvl = q.popleft()

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if not xmi<=nx<=xma or not ymi<=ny<=yma:
                    continue
                if m[nx][ny] > lvl+1:
                    m[nx][ny] = lvl+1
                    q.append((nx, ny, lvl+1))
        #pprint(m)
        return m



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
    r = so.minKnightMoves(*args, **kw)
    print(r)


x = 2
y = 1

x = 5
y = 5


x = -76
y = 144
"""
x = 209
y = -58

"""

x = 0
y = 1


run(x, y)