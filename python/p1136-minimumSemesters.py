import pprint
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq
from collections import deque
from datetime import datetime 
time_start = datetime.now()

class Solution:
    def minimumSemesters(self, n: int, relations: list[list[int]]) -> int:
        
        adjList = defaultdict(list)
        indeg = [0] * (n+1)
        for pr, ne in relations:
            adjList[ne].append(pr)
            indeg[pr] += 1

        #print(adjList)
        #print(indeg)

        sem = []
        for i in range(1,n+1):
            if indeg[i] == 0: sem.append(i)
        if not sem: return -1
        #print(sem)

        sem_num = 1
        while 1:
            semn = []
            for i in sem:
                for j in adjList[i]:
                    indeg[j] -= 1
                    if indeg[j] == 0: semn.append(j)
            
            if not semn: break
            sem = semn
            sem_num += 1

        #print(indeg)
        if indeg.count(0) < n+1: return -1
        return sem_num


n = 3
relations = [[1,3],[2,3]]

n = 4
relations = [[1,2],[2,3],[3,1],[1,4]]

so = Solution()
r = so.minimumSemesters(n, relations)
pp.pprint(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)