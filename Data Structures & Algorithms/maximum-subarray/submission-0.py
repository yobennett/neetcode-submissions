class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestMax, currMax = nums[0], 0
        for num in nums:
            if currMax < 0:
                currMax = 0
            currMax += num
            bestMax = max(bestMax, currMax)
        return bestMax