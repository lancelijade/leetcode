#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        def isEdge(x:int, y:int) -> bool:
            dirs = ((0,1), (1,0), (0, -1), (-1, 0))
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    return True
            return False


        def bfs() -> int:
            dirs = ((0,1), (1,0), (0, -1), (-1, 0))
            while q:
                x, y, step = q.popleft()
                if isEdge(x, y) and step != 0:
                    return step

                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if nx>=0 and nx<m and ny>=0 and ny<n and maze[nx][ny] == '.':
                        if isEdge(nx, ny):
                            return step+1
                        q.append((nx, ny, step+1))
                        maze[nx][ny] = ':'
            return -1


        m, n = len(maze), len(maze[0])

        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = ':'
        r = bfs()

        return r
        


# @lc code=end


if __name__ == "__main__":

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
        r = so.nearestExit(*args, **kw)
        print(r)


    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]

    #maze = [["+","+","+"],[".",".","."],["+","+","+"]]
    #entrance = [1,0]

    maze = [[".","+"]]
    entrance = [0,0]

    maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".","+",".","+"],["+","+","+","+","+",".","+"]]
    entrance = [0,1]


    run(maze, entrance)

