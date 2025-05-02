# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parent[rootY] = rootX
            elif self.size[rootX] == self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += 1
            else:
                self.parent[rootX] = rootY

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n): 
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return len(set(uf.find(i) for i in range(n)))
