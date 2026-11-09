class Solution:
    # dynamic programming bottom-up
    def rob(self, nums: List[int]) -> int:
        # no houses
        if not nums:
            return 0

        # only one house
        if len(nums) == 1:
            return nums[0]

        # dp is max money up to i
        dp = [0] * len(nums)
        dp[0] = nums[0]                 # only one house
        dp[1] = max(nums[0], nums[1])   # max btw house 0 and house 1

        # build up for each house i >= 2
        # two choices:
        # choice 1: rob prev house [i - 1]
        # choise 2: rob curr house and house before prev house
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        # max money is last result
        return dp[-1]