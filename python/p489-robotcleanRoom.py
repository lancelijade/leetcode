# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
from pprint import pprint, pp
from var_dump import var_dump


class Robot:
    def __init__(self, room: list[list[int]], x: int, y: int):
        'room matrix: 0 blocked, 1 accessible'
        self.room = room

        'current pos'
        self.x, self.y = x, y

        'matrix len m * n'
        self.m, self.n = len(room), len(room[0])

        'clean status, -1 for cleaned'
        self.cl = [room[i].copy() for i in range(self.m)]

        'dir: 0 up, 1 right, 2 down, 3 left'
        self.dir = 0
        self.dirs = [(-1,0), (0,1), (1,0), (0,-1)]


    def move(self) -> bool:
        nx = self.x + self.dirs[self.dir][0]
        ny = self.y + self.dirs[self.dir][1]
        if nx>=0 and ny>=0 and nx<self.m and ny<self.n and self.room[nx][ny]==1:
            self.x = nx
            self.y = ny
            return True
        else:
            return False


    def turnLeft(self):
        self.dir -= 1
        if self.dir == -1: self.dir = 3


    def turnRight(self):
        self.dir += 1
        if self.dir == 4: self.dir = 0


    def clean(self) -> bool:
        if self.cl[self.x][self.y] == 0:
            return False
        self.cl[self.x][self.y] = -1
        return True




class Solution:

    def cleanRoom(self, robot: Robot):

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrace(pos, dir):
            visited.add(pos)
            robot.clean()
            x, y = pos[0], pos[1]
            for i in range(4):
                ndir = (dir + i) % 4
                nx, ny = x + dirs[ndir][0], y + dirs[ndir][1]
                if (nx, ny) not in visited and robot.move():
                    backtrace((nx, ny), ndir)
                    go_back()
                robot.turnRight()


        'dir: 0 up, 1 right, 2 down, 3 left'
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]

        visited = set()
        backtrace((0,0), 0)


room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]]
row = 1
col = 3

robot = Robot(room, row, col)
so = Solution()
so.cleanRoom(robot)

pprint(robot.room)
pprint(robot.cl)

