import pprint

pp = pprint.PrettyPrinter()
from var_dump import var_dump


class UnionFind:
    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.part = size

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
            self.part -= 1

    def connected(self, x, y) -> int:
        return self.find(x) == self.find(y)

    def getpart(self) -> int:
        return self.part


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        uf = UnionFind(len(isConnected))

        le = len(isConnected)
        i = 0
        while i < le:
            j = i + 1
            while j < le:
                if j>i and isConnected[i][j]: uf.union(i, j)
                j += 1
            i += 1

        return uf.getpart()


isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#isConnected = [[1,0,0],[0,1,0],[0,0,1]]

so = Solution()
r = so.findCircleNum(isConnected)
pp.pprint(r)
