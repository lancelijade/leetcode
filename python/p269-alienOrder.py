import pprint
from executing import Source
pp = pprint.PrettyPrinter()
from var_dump import var_dump
from collections import defaultdict
import math
import heapq
import re
from collections import deque
from datetime import datetime 
time_start = datetime.now()


class Solution:
    def alienOrder(self, words: list[str]) -> str:

        adjList = defaultdict(list)
        indeg = {}
        for i, s in enumerate(words):
            sa = list(s)
            for c in sa:
                if c not in indeg:
                    indeg[c] = 0

            if i > 0:
                sp = list(words[i-1])
                #print(sp, sa)
                for c in sp:
                    if c not in indeg:
                        indeg[c] = 0
                lens = len(s)
                lenp = len(words[i-1])
                for j in range(max(lens, lenp)):
                    if lens!=lenp:
                        if j>lens-1:
                            return ""
                        elif j>lenp-1:
                            break

                    if sp[j] != sa[j]:
                        if sa[j] not in adjList[sp[j]]:
                            adjList[sp[j]].append(sa[j])
                            indeg[sa[j]] += 1
                        break

        #print("adjList = ", adjList)
        #print("indeg =", indeg)

        q = deque()
        for k, v in indeg.items():
            if v == 0: q.append(k)

        #print("q =", q)

        r = ""
        while q:
            c = q.popleft()
            r += c

            for ne in adjList[c]:
                indeg[ne] -= 1
                if indeg[ne] == 0: q.append(ne)

        #print(r)
        if len(r) == len(indeg):
            return r
        else:
            return ""


words = ["wrt","wrf","er","ett","rftt"]
words = ["z","x"]
words = ["z","x","z"]
words = []
words = ["ac","ab","zc","zb"]
words = ["abc","ab"]
words = ["wrt","wrf","er","ett","rftt","te"]
words = []



so = Solution()
r = so.alienOrder(words)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)