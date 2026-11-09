class Solution:
    # sliding window
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float("inf")
        L, total = 0, 0

        # advance R index
        for R in range(len(nums)):
            # increase total
            total += nums[R]
            # total at target or greater
            # check to see if subarray still gte target when removing nums[L]
            while total >= target:
                # compare length
                length = min(length, R - L + 1)
                # exclude leftmost
                total -= nums[L]
                # advance L index
                L += 1
        
        return 0 if length == float("inf") else length