#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
import heapq
import math

# @lc code=start
class Solution2:

    def djtable(self, n: int, k: int):
        self.t = [[math.inf, -1] for _ in range(n+1)]
        self.t[k][0] = 0

    def djfind(self):
        dis = math.inf
        r = None

        for node, d in enumerate(self.t):
            #print(node, d)
            if node in self.visited: continue
            if d[0] < dis: 
                r = node
                dis = d[0]
        return r


    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        self.djtable(n, k)
        self.visited = [k]

        adjList = [[math.inf] * (n+1) for _ in range(n+1)]
        for src, tgt, time in times:
            adjList[src][tgt] = time
            if src == k:
                self.t[tgt] = [time, k]

        #pp.pprint(self.t)
        #pp.pprint(adjList)

        while len(self.visited) < n:
            node = self.djfind()
            if not node: break
            #print("node=", node)
            self.visited.append(node)

            for tgt, time in enumerate(adjList[node]):
                if self.t[tgt][0] > time + self.t[node][0]:
                    self.t[tgt] = [time + self.t[node][0], node]

            #pp.pprint(self.t)


        #pp.pprint(self.t[1:])
        r = max(self.t[1:])[0]
        if r == math.inf: return -1
        else: return r


class Solution:
    
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dj = []
        visited = set()
        visited.add(k)
        dis = [(math.inf, -1) for _ in range(n+1)]
        dis[k] = (0, -1)

        adjList = [[math.inf] * (n+1) for _ in range(n+1)]
        for src, tgt, time in times:
            adjList[src][tgt] = time
            if src == k:
                heapq.heappush(dj, (time, tgt))
                dis[tgt] = (time, src)

        while len(visited) < n and dj:
            time0, node = heapq.heappop(dj)
            if node in visited: continue
            visited.add(node)

            for tgt, time in enumerate(adjList[node]):
                if dis[tgt][0] > time + time0:
                    dis[tgt] = (time + time0, node)
                    heapq.heappush(dj, (time+time0, tgt))

        r = max(dis[1:])[0]
        if r == math.inf: return -1
        else: return r
        
        
# @lc code=end


times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

#times = [[1,2,1]]
#n = 2
#k = 1

times = [[1,2,1]]
n = 2
k = 2

times = [[1,3,68],[1,4,20],[4,1,65],[3,2,74],[2,1,44],[3,4,61],[4,3,68],[3,1,26],[5,1,60],[5,3,3],[4,5,5],[2,5,36],[2,3,94],[1,2,0],[3,5,90],[2,4,28],[4,2,12],[5,4,52],[5,2,85],[1,5,42]]
n = 5
k = 4       # 34

so = Solution()
r = so.networkDelayTime(times, n, k)
pp.pprint(r)