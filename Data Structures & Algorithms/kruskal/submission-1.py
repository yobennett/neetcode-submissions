class UnionFind:

    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v: int) -> int:
        if v != self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, n1: int, n2: int) -> bool:
        parent1, parent2 = self.find(n1), self.find(n2)
        rank1, rank2 = self.rank[parent1], self.rank[parent2]

        # already have same parent
        # return false if operation can't be completed
        if parent1 == parent2:
            return False

        if rank1 < rank2:
            self.parent[parent1] = parent2
        elif rank1 > rank2:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1
        return True

class Solution:
    # Kruskal's with UnionFind
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # setup
        # push all edges onto heap
        minHeap = []
        for u, v, w in edges:
            heapq.heappush(minHeap, [w, u, v])

        # initialize
        uf = UnionFind(n)

        # iterate through min heap
        # union vertices, increment result if successful
        result = 0
        components = n
        while minHeap and components > 1:
            w1, u1, v1 = heapq.heappop(minHeap)
            if uf.union(u1, v1):
                result += w1
                components -= 1

        return result if components == 1 else -1