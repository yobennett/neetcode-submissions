class Solution:
    # dynamic programming top-down w/ memoization
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            # out of bounds
            if i < 0 or i >= len(nums):
                return 0

            # use cached result for i if found
            if memo[i] != -1:
                return memo[i]

            # cache result for i
            memo[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))

            return memo[i]

        return dfs(0)