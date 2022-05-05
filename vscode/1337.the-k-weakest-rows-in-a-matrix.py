#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
import heapq


class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        m = len(mat)
        t = []
        for i in range(m):
            t.append((mat[i].count(1), i))
        heapq.heapify(t)
        return [y for x,y in heapq.nsmallest(k, t)]
        
# @lc code=end

mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 3

#mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
#k = 2

#mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
#k = 3

so = Solution()
r = so.kWeakestRows(mat, k)
print(r)