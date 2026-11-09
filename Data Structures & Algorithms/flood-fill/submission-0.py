class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingPixel = image[sr][sc]
        
        # starting pixel already colored
        if startingPixel == color:
            return image

        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):
            # check pixel in bounds and original color
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or image[r][c] != startingPixel:
                return

            # set color
            image[r][c] = color

            # check other directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image