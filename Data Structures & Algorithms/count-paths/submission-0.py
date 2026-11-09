class Solution:
    # dynamic programming, bottom-up
    def uniquePaths(self, m: int, n: int) -> int:
        # init prevRow so that we can make it work
        # for the last row
        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            currRow = [0] * n

            # only one path from last column
            # since we can only move down and right
            currRow[n - 1] = 1

            # skip last column
            for c in range(n - 2, -1 , -1):
                currRow[c] = currRow[c + 1] + prevRow[c]
            
            # update prevRow
            prevRow = currRow

        # answer is first column in the first row, 
        # which is now prevRow
        return prevRow[0]
