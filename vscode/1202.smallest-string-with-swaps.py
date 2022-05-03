#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

from collections import defaultdict
from var_dump import var_dump

import pprint
pp = pprint.PrettyPrinter()
from datetime import datetime 
time_start = datetime.now()


# @lc code=start
from sortedcontainers import SortedList

class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x: int) -> int:
        if x == self.root[x]: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]        

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y) -> int:
        return self.find(x) == self.find(y)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        
        uf = UnionFind(len(s))
        for i, j in pairs:
            uf.union(i, j)

        #var_dump(uf)

        di = defaultdict(SortedList)
        li = defaultdict(list)
        for i, ch in enumerate(s):
            g = uf.find(i)
            di[g].add(ch)
            li[g].append(i)

        #print(di)
        #print(li)

        r = [''] * len(s)
        for g, chs in di.items():
            #print(g, chs)
            for i, ch in enumerate(chs):
                r[li[g][i]] = ch

        #print(r)
        return "".join(r)

        
# @lc code=end

s = "dcab"
pairs = [[0,3],[1,2]]

s = "dcab"
pairs = [[0,3],[1,2],[0,2]]

s = "cba"
pairs = [[0,1],[1,2]]

s = "pwqlmqm"
pairs = [[5,3],[3,0],[5,1],[1,1],[1,5],[3,0],[0,2]]

so = Solution()
r = so.smallestStringWithSwaps(s, pairs)
print(r)


time_end = datetime.now()
print("---\ntime cost:",time_end-time_start)