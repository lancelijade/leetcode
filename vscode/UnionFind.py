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
