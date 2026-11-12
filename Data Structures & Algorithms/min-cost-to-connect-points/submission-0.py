class Solution:
    # Prim's for a minimum spanning tree
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # setup
        adj = {}
        for i in range(len(points)):
            x, y = points[i]
            adj[(x, y)] = []
        # cost is manhattan distance) between each 
        # edges for both (xi, yi) and (xj, yj)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    xi, yi = points[i]
                    xj, yj = points[j]
                    w = abs(xi - xj) + abs(yi - yj)
                    adj[(xi, yi)].append((xj, yj, w))
                    adj[(xj, yj)].append((xi, yi, w))

        # initialize
        minHeap = [ (0, (points[0][0], points[0][1])) ]
        visit = set()

        # BFS, skip if already visited
        result = 0
        while minHeap and len(visit) < len(adj):
            w1, coord1 = heapq.heappop(minHeap)
            if coord1 in visit:
                continue

            visit.add(coord1)
            result += w1

            # iterate through neighbords
            # skip if already visited
            for x2, y2, w2 in adj[coord1]:
                coord2 = (x2, y2)
                if coord2 not in visit:
                    heapq.heappush(minHeap, (w2, coord2))

        return result if len(visit) == len(adj) else -1