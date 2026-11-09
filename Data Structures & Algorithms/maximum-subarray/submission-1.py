class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestMax, currMax = nums[0], 0

        for num in nums:
            currMax = max(currMax + num, num)
            bestMax = max(bestMax, currMax)

        return bestMax