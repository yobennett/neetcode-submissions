class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M, N = capacity, len(profit)

        dp = [0] * (M + 1)

        for i in range(N):

            p = profit[i]
            w = weight[i]

            # left-to-right to read new values so dp[j - w] may already 
            # include item `i`, letting it be reused
            # start at w, end at M
            for j in range(w, M + 1):

                # maximize profit by either skipping or taking item at i
                dp[j] = max(
                    dp[j],          # skip
                    dp[j - w] + p   # take
                )

        return dp[M]