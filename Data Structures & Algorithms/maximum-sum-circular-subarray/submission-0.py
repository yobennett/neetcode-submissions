class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        bestMax, currMax = nums[0], 0
        bestMin, currMin = nums[0], 0
        total = 0

        for num in nums:
            currMax = max(currMax + num, num)
            bestMax = max(bestMax, currMax)

            currMin = min(currMin + num, num)
            bestMin = min(bestMin, currMin)

            total += num

        # all negative, use non-wrapping Kadane
        if bestMax < 0:
            return bestMax

        return max(bestMax, total - bestMin)
