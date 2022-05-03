#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
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
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        courses = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            courses[b].append(a)
            indegrees[a] += 1

        #pp.pprint(courses)
        #pp.pprint(indegrees)

        q = deque()
        for i, n in enumerate(indegrees):
            if n == 0: q.append(i)
        if not q: return []

        #print(q)

        r = []
        while q:
            c = q.popleft()
            r.append(c)

            for nc in courses[c]:
                indegrees[nc] -= 1
                if indegrees[nc] == 0: q.append(nc)

        if len(r) == numCourses: return r
        else: return []

        
# @lc code=end


numCourses = 2
prerequisites = [[1,0]]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]

#numCourses = 2
#prerequisites = []

so = Solution()
r = so.findOrder(numCourses, prerequisites)
pp.pprint(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)