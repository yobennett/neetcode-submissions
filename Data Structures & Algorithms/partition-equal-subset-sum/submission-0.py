class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # read right-to-left to read old cells before overwriting
            # stop bound is `num - 1` since we don't need negative sums and negative indexes would wrap and give unrelated results
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]