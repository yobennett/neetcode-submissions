class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # set up with adjacency list
        adj = {}
        for i in range(n):
            adj[i] = []
        # populate with s -> d + w
        for s, d, w in edges:
            adj[s].append((d, w))

        # track shortest path to each dst from src
        shortest = {}

        # min heap for selecting next hop with lowest weight
        # initialize with src
        minHeap = [(0, src)]

        while minHeap:
            # pop the min heap for edge with next lowest weight
            w1, n1 = heapq.heappop(minHeap)

            # skip if already visited
            if n1 in shortest:
                continue

            # otherwise add to visited
            shortest[n1] = w1

            # push each neighbor onto the heap
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        # set to -1 if never visited
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest