class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      # initialize grid
        dp = [
            [0] * (n + 1) for _ in range(m + 1)
        ]

        for s in strs:

            # count zeros and ones for current s
            zeros = s.count("0")
            ones = s.count("1")

            # traverse right-to-left for both dimensions
            # stop at zeros
            for z in range(m, zeros - 1, -1):
                # stop at ones
                for o in range(n, ones - 1, -1):
                    # max compares 
                    # skipping `s`
                    # vs
                    # best subset using the budget leftover after taking `s`
                    dp[z][o] = max(
                        dp[z][o],                   # skip
                        dp[z - zeros][o - ones] + 1 # take
                        )

        return dp[m][n]  