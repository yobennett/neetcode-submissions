class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # setup with adj list, shortest/visited, and min heap, seed with source node
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for s, d, t in times:
            adj[s].append((t, d))

        shortest = {}

        minHeap = [(0, k)]

        while minHeap:
            # pop edge with lowest weight
            t1, n1 = heapq.heappop(minHeap)

            # skip if already visited
            if n1 in shortest:
                continue

            # add to shortest/visited
            shortest[n1] = t1

            # iterate through neighbors, add weights (incl. prev weights)
            for t2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, n2))

        # shortest should have n entries (including k)
        # -1 otherwise
        if len(shortest) != n:
            return -1

        return max(shortest.values())