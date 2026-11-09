class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, n):
        curr = n
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr

    def union(self, n1, n2):
        root1, root2 = self.find(n1), self.find(n2)

        if root1 == root2:
            return False

        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1

        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2

        else:
            self.parent[root2] = root1
            self.rank[root1] += self.rank[root2]
        
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        result = n # initially each node is a separate component
        for u, v in edges:
            if uf.union(u, v):
                # decrement running count of components if union succeeds
                result -= 1
        return result
