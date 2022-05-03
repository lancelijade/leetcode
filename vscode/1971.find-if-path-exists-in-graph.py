#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque


# @lc code=start
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:

        if source == destination: return True

        adjList = [[] for _ in range(n)]
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        q = deque([source])
        seen = []

        while q:
            node = q.popleft()

            if node in seen: continue
            seen.append(node)

            for i in adjList[node]:
                if i == destination: return True
                if i not in seen: q.append(i)
        
        return False
        
# @lc code=end


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

"""
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
"""

so = Solution()
r = so.validPath(n, edges, source, destination)
pp.pprint(r)