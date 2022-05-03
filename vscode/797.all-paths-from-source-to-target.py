#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import deque

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:

        n = len(graph)
        q = deque()
        path = [0]
        q.append(path)
        r = []

        while q:
            path = q.popleft()

            for i in graph[path[-1]]:

                path.append(i)
                if i == n-1:
                    r.append(path.copy())
                else:
                    q.append(path.copy())
                path.pop()

        return r
        
# @lc code=end

graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]

so = Solution()
r = so.allPathsSourceTarget(graph)
pp.pprint(r)