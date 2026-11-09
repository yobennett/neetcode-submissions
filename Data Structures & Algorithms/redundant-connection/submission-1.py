class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initialize
        # each edge is its own parent, rank is 1 by default
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]
            while p !=  parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        # return True if not yet in the same connected component
        # find parent for each given node from an edge
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # same parents, already connected
            if p1 == p2:
                return False
            # n1 parent's rank is greater
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            # n2 parent's rank is greater
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        # add edges using union
        for n1, n2 in edges:
            # return edge with n1 and n2 if union returns True, already connected component
            if not union(n1, n2):
                return [n1, n2]