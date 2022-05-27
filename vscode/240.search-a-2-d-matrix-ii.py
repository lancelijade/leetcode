#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
from functools import cache


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        @cache
        def search(x0, y0, x1, y1):
            #print(x0, y0, x1, y1)
            if matrix[x0][y0] == target or matrix[x1][y1] == target:
                return True
            if x1 == x0 and y1 == y0:
                return True if matrix[x0][y0] == target else False
            if x1 < x0 or y1 < y0:
                return False
                    
            x = (x1 + x0) // 2
            y = (y1 + y0) // 2
            #print(x, y)
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                #print("less")
                r = search(x0, y0, x, y)
                if r: return r
                if x+1 <= x1 and y-1 >= y0:
                    r = search(x+1, y0, x1, y-1)
                    if r: return r
                if y+1 <= y1 and x-1 >= x0:
                    r = search(x0, y+1, x-1, y1)
                    if r: return r
                return False
            else:
                #print("greater")
                if (x, y) != (x0, y0):
                    r = search(x, y, x1, y1)
                    if r: return r
                if x+1 <= x1 and y+1 <= y1:
                    r = search(x0, y+1, x+1, y1)
                    if r: return r
                if y+1 <= y1 and x+1 <= x1:
                    r = search(x+1, y0, x1, y+1)
                    if r: return r
                return False


        m, n = len(matrix), len(matrix[0])
        return search(0, 0, m-1, n-1)




# @lc code=end

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5


matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
"""

matrix = [[-5]]
target = -2

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 0

matrix = [[-1,3]]
target = 3

matrix = [[1,4],[2,5]]
target = 2
"""


so = Solution()
r = so.searchMatrix(matrix, target)
print(r)