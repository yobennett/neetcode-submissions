class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # obstacles at start or end
        if (obstacleGrid[0][0] == 1) or (obstacleGrid[-1][-1] == 1):
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # table w/ extra row and column for boundary handling
        dp  = [[0] * (n + 1) for _ in range(m + 1)]

        # exactly one path from bottom-right
        dp[m - 1][n - 1] = 1

        for r in range(m - 1, -1, -1):

            for c in range(n - 1, -1 , -1):
                # if obstacle
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] += dp[r + 1][c] # from prev row
                    dp[r][c] += dp[r][c + 1] # from prev col

        # answer is first column in the first row
        return dp[0][0]
        