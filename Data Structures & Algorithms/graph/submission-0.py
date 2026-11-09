class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if not src in self.adj_list:
            self.adj_list[src] = set()
        if not dst in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        if dst in self.adj_list[src]:
            self.adj_list[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        return self._dfs(src, dst, set())

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True
        visited.add(src)
        for neighbor in self.adj_list[src]:
            if neighbor not in visited:
                if self._dfs(neighbor, dst, visited):
                    return True
        return False
