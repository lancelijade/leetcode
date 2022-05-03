#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq

# @lc code=start
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        adjList = defaultdict(dict)
        for f in flights:
            adjList[f[1]][f[0]] = f[2]

        pp.pprint(adjList)

        trip = [[math.inf for _ in range(n)] for _ in range(k+2)]
        trip[0][src] = 0
        #pp.pprint(trip)

        for i in range(1, k+2):
            for j in range (n):
                if j == src: 
                    trip[i][j] = 0
                else:
                    if j in adjList:
                        for d in adjList[j]:
                            trip[i][j] = min(trip[i][j], trip[i-1][d] + adjList[j][d])

        #pp.pprint(trip)
        
        r = trip[k+1][dst]
        if r == math.inf: return -1
        return r


class Solution3:    # Dj's 不适用，因为步数限制
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:

        q = []
        
        dis = [(math.inf, -1) for _ in range(n+1)]
        dis[src] = (0, 0)

        adjList = defaultdict(dict)
        for fr, tgt, price in flights:
            adjList[fr][tgt] = price
            if fr == src:
                heapq.heappush(q, (price, tgt, 1))
                dis[tgt] = (price, 1)

        #visited = set()
        #visited.add(src)

        pp.pprint(adjList)
        print(dis)
        print(q)
        print('---')

        while q:
            price0, src, lvl = heapq.heappop(q)

            if lvl>k: continue
            #visited.add(src)

            if src in adjList:
                for tgt, price in adjList[src].items():
                    print("src=", src, "tgt=", tgt, "price=", price)
                    if dis[tgt][0] > price0 + price:
                        dis[tgt] = (price0 + price, lvl+1)
                        if lvl<k:
                            heapq.heappush(q, (price0 + price, tgt, lvl+1))

                    print(dis)
                    print(q)
                    print('---')

        #pp.pprint(dis)
        r = dis[dst][0]
        if r == math.inf: return -1
        return r

# @lc code=end

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0



n = 5
flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
src = 2
dst = 1
k = 1
#"""
n = 17
flights = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
src = 13
dst = 4
k = 13
#"""

n = 5
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0
dst = 2
k = 2


so = Solution()
r = so.findCheapestPrice(n, flights, src, dst, k)
pp.pprint(r)