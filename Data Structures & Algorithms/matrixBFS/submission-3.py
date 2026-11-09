class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        # check that top-left and bottom-right are land:
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        queue.append((0, 0))
        visit.add((0, 0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # at bottom-right
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if r + dr < 0 or r + dr >= ROWS or c + dc < 0 or c + dc >= COLS or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue # skip out of bounds or already visited or land
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))

            length += 1

        return -1