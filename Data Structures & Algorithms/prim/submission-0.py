class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # setup adj list, min heap, visit set
        adj = {}
        for i in range(n):
            adj[i] = []
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        minHeap = []
        visit = set()

        # initialize with first vertex and weight 0
        minHeap.append([0, 0])

        # BFS while popping heap, skip if already visited
        # iterate through neighbors, skip if already visited
        result = 0
        while minHeap and len(visit) < n:

            w1, v1 = heapq.heappop(minHeap)

            # skip if already visited
            if v1 in visit:
                continue

            result += w1
            visit.add(v1)

            for v2, w2 in adj[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, [w2, v2])
        
        # return result if visited all vertices
        return result if len(visit) == n else -1