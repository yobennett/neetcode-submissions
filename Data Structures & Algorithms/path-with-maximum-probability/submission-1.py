class Solution:
    # Dijkstra
    # with max heap
    # like shortest path but max probability instead
    # products of success probabilities for each edge
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # setup
        adj = {}
        for i in range(n):
            adj[i] = []
        for i, edge in enumerate(edges):
            s, d = edge
            # graph is undirected so need src -> dst and dst -> src with same prob
            adj[s].append((d, succProb[i]))
            adj[d].append((s, succProb[i]))

        visited = {}

        # seed with start
        maxHeap = [(-1, start_node)]

        while maxHeap:
            p1, n1 = heapq.heappop(maxHeap)
            p1 = p1 * -1

            # skip if visited
            if n1 in visited:
                continue

            # add to visited
            visited[n1] = p1

            # reached target end, return probability
            if n1 == end_node:
                return p1

            for n2, p2 in adj[n1]:
                if n2 not in visited:
                    # push probability of p1 and p2 with -1 since max heap
                    heapq.heappush(maxHeap, (p1 * p2 * -1, n2))

        return 0