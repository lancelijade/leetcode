#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        t = []
        heapq.heapify(t)
        for x, y in points:
            heapq.heappush(t, (x*x+y*y, [x, y]))
        return [p for n, p in heapq.nsmallest(k, t)]

        
# @lc code=end

points = [[1,3],[-2,2]]
k = 1

points = [[3,3],[5,-1],[-2,4]]
k = 2

so = Solution()
r = so.kClosest(points, k)
print(r)