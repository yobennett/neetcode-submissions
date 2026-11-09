class Solution:
    # dynamic programming, bottom-up
    def climbStairs(self, n: int) -> int:
        # one or two stairs
        if n <= 2:
            return n

        # TODO why n+1
        dp = [0] * (n + 1)
        dp[1] = 1 # only one way to go up 1 stair
        dp[2] = 2 # only two ways to go up 2 stairs (1+1 or 2)

        # build for 3+ stairs
        # number of ways = # ways from 1 step back + # ways from 2 steps back 
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        # ways from n is result 
        return dp[n]
