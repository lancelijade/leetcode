import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        
        r = [([0] * n) for _ in range(n)]
        #pp.pprint(r)

        i = 0
        j = 0
        dir = [0, 1]
        cnt = 1

        while cnt <= n*n:
            if r[i][j] == 0:
                r[i][j] = cnt
            #pp.pprint(r)

            if i+dir[0]==n or i+dir[0]<0 or j+dir[1]==n or j+dir[1]<0 or r[i+dir[0]][j+dir[1]] != 0:
                match dir:
                    case [0, 1]: dir = [1, 0]
                    case [1, 0]: dir = [0, -1]
                    case [0, -1]: dir = [-1, 0]
                    case [-1, 0]: dir = [0, 1]

            i += dir[0]
            j += dir[1]
            cnt += 1

        return r


n = 5

so = Solution()
r = so.generateMatrix(n)
pp.pprint(r)