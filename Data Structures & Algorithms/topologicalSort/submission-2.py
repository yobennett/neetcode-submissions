class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # setup adjacency list
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)

        result = []

        # already visited
        visited = set()

        # visiting now
        # current path
        visiting = set()

        def dfs(src: int):
            # already visited
            # True since already visited, not cycle
            if src in visited:
                return True

            # cycle
            # False if visiting in current path
            if src in visiting:
                return False

            # init
            visiting.add(src)

            # recursive call
            for neighbor in adj[src]:
                # cycle detected
                if not dfs(neighbor):
                    return False

            # cleanup
            visiting.remove(src)
            visited.add(src)

            # add to result
            result.append(src)

            return True

        # iterate for each entry in adj list
        for i in range(n):
            if not dfs(i):
                return []

        return result[::-1]