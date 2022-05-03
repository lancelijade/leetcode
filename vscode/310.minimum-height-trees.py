#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq
from collections import deque
from datetime import datetime 
time_start = datetime.now()


# @lc code=start
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        if n <= 2: return [i for i in range(n)]

        adjList = [set() for _ in range(n)]
        deg = [0] * n
        for src, tgt in edges:
            adjList[tgt].add(src)
            adjList[src].add(tgt)
            deg[src] += 1
            deg[tgt] += 1
            
        #print(adjList)
        #print(deg)

        leaves = []
        for i, num in enumerate(deg):
            if num == 1: leaves.append(i)

        #print(leaves)
        #print(deg.count(1)+deg.count(0))

        while n - deg.count(1) - deg.count(0)>2:

            lnew = []
            for node in leaves:
                for tgt in adjList[node]:
                    deg[tgt] -= 1
                    if deg[tgt] == 1: 
                        lnew.append(tgt)
            leaves = lnew

            #print(deg)
            #print(deg.count(1)+deg.count(0))

        r = []
        for i, num in enumerate(deg):
            if num>1: r.append(i)
        return r

        
# @lc code=end

n = 4
edges = [[1,0],[1,2],[1,3]]

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

"""
n = 2
edges = [[0,1]]

n = 6
edges = [[0,1],[0,2],[0,3],[3,4],[4,5]]
"""

n = 8
edges = [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]

so = Solution()
r = so.findMinHeightTrees(n, edges)
pp.pprint(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)

