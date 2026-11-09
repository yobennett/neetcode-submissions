class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = 0

        visit = set()

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == "0" or (r, c) in visit:
                return

            # sink land
            #grid[r][c] = "0"
            # or add to visit
            visit.add((r, c))

            # explore each direction
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # DFS for each land pixel
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    result += 1
        
        return result