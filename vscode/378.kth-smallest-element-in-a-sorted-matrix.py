#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        r = []
        heapq.heapify(r)
        for j in range(n):
            for i in range(n):
                heapq.heappush(r, -matrix[i][j])
                if len(r) > k: 
                    heapq.heappop(r)
        
        return -r[0]

        
# @lc code=end

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

"""
matrix = [[-5]]
k = 1

matrix = [[1,2],[3,3]]
k = 2
"""

so = Solution()
r = so.kthSmallest(matrix, k)
print(r)
