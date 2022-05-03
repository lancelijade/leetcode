#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
from collections import defaultdict
from var_dump import var_dump

# @lc code=start
class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.eq = defaultdict(dict)

    def find(self, x: int) -> int:
        if x == self.root[x]: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]        

    def union(self, x: int, y: int, val: float):
        self.rec(x, y, val)
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

    def rec(self, x: int, y: int, val: float):
        if x not in self.eq:
            self.eq[x] = {}
        if y not in self.eq:
            self.eq[y] = {}
        self.eq[x][y] = val
        self.eq[y][x] = 1 / val

    def div(self, x: int, y: int, path=[]) -> float:
        if x in self.eq and y in self.eq[x]:
            return self.eq[x][y]
        for i in self.eq[x]:
            if i not in path:
                r = self.div(i, y, path+[x])
                if r != -1.0:
                    self.eq[x][y] = self.eq[x][i] * self.eq[i][y]
                    self.eq[y][x] = 1 / self.eq[x][y]
                    return self.eq[x][y]
        return -1.0


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        uf = UnionFind(len(equations)*2)
        dct = {}
        i = 0
        for j, eq in enumerate(equations):
            x = eq[0]
            y = eq[1]
            if x not in dct: 
                dct[x] = i
                i += 1
            if y not in dct:
                dct[y] = i
                i += 1
            uf.union(dct[x], dct[y], values[j])

        #print(dct)
        #var_dump(uf)

        r = []
        for x, y in queries:
            if x not in dct or y not in dct or not uf.connected(dct[x], dct[y]): 
                r.append(-1.0)
                continue
            r.append(uf.div(dct[x], dct[y]))

        #print(uf.eq)
        return r
        
# @lc code=end


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]

equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

so = Solution()
r = so.calcEquation(equations, values, queries)
print(r)