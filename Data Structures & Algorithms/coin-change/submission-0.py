class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        M = amount + 1
        
        # initial grid
        # dp[j] is the fewest coins to make amount j
        sentinel = float('inf') # impossible
        dp = [sentinel] * M

        # seed base case, zero coins to make amount 0
        dp[0] = 0

        for coin in coins:
            for j in range(coin, M):
                dp[j] = min(
                    dp[j],              # skip
                    dp[j - coin] + 1    # take
                )

        return dp[amount] if dp[amount] != sentinel else -1