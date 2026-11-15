class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        M = amount + 1

        # init grid
        dp = [0] * M

        # seed base case, 1 combination of coins to make amount 0
        dp[0] = 1

        for coin in coins:
            for j in range(coin, M):
                # number of combinations of coins that make amount j
                # is the sum of both with (take) and without (skip)  
                dp[j] = dp[j] + dp[j - coin]

        return dp[amount]    