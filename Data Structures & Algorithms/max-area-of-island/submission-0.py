class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return 0

            # track visit (or sink land)
            visit.add((r, c))

            # explore each direction and increment
            count = 1
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            return count

        # DFS for each land pixel
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))

        return area