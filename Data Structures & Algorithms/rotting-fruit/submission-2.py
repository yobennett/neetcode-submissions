class Solution:
    # 2 1 1
    # 1 1 1
    # 0 1 2

    # 2 2 1
    # 2 1 2
    # 0 2 2

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()

        def bfs(fresh):
            print("bfs initial fresh=", fresh)
            minutes = 0
            while queue and fresh > 0:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        rNew, cNew = r + dr, c + dc
                        if rNew < 0 or rNew >= ROWS or cNew < 0 or cNew >= COLS or (rNew, cNew) in visit or grid[rNew][cNew] != 1:
                            continue
                        
                        queue.append((rNew, cNew))
                        visit.add((rNew, cNew))
                        grid[rNew][cNew] = 2 # turn fresh to rotten
                        fresh -= 1

                minutes += 1

            return minutes if fresh == 0 else -1

        # scan grid for rotten
        freshInitial = 0
        for r in range(ROWS):
            for c in range(COLS):
                # fresh
                if grid[r][c] == 1:
                    freshInitial += 1
                # rotten
                elif grid[r][c] == 2:
                    visit.add((r, c))
                    queue.append((r, c))

        # impossible, no initial fresh fruit to be adjancent to rotten fruit
        if freshInitial == 0:
            return 0
        else:
            return bfs(freshInitial)