#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
from collections import deque


class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:

        def dfs(node: int, newrank: int) -> int:
            #print("dfs entry:", node, newrank)
            if rank[node] is not None: return rank[node]
            rank[node] = newrank
            minrank = newrank + 1
            for i in adjList[node]:
                if rank[i] is not None and rank[i] == newrank-1: continue
                rrank = dfs(i, newrank + 1)
                if rrank <= newrank:     #found circle
                    #print(adjList, node, i)
                    del conn[(min(node, i), max(node, i))]
                minrank = min(minrank, rrank)
            return minrank


        adjList = {i: [] for i in range(n)}
        conn = {}
        for a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
            conn[(min(a, b), max(a, b))] = 1
        #print(adjList)
        #print(conn)

        rank = [None] * n

        dfs(0, 0)
        #print(conn)
        #print(rank)

        r = []
        for c in conn.keys():
            r.append(c)
        return r

        
# @lc code=end

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

#n = 6
#connections = [[0,1],[0,2],[1,2],[0,3],[3,4],[3,5],[4,5]]

#n = 2
#connections = [[0,1]]

so = Solution()
r = so.criticalConnections(n, connections)
print(r)