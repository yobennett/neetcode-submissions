class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # start/end blocked, no possible path
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        visit = set()
        queue = deque()

        visit.add((0, 0))
        queue.append((0, 0))
        length = 1 # set to 1 since start is visited

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # at bottom-right target
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                for dr, dc in neighbors:
                    rNew, cNew = r + dr, c + dc

                    if rNew < 0 or rNew >= ROWS or cNew < 0 or cNew >= COLS or (rNew, cNew) in visit or grid[rNew][cNew] == 1:
                        continue

                    visit.add((rNew, cNew))
                    queue.append((rNew, cNew))

            length += 1
        
        return -1