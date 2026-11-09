class Solution:
    # prefix sum optimal
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            # right sum is the total without leftSum and the current num
            rightSum = total - leftSum - nums[i]
            # found match
            if leftSum == rightSum:
                return i
            # continue to build prefix sum
            leftSum += nums[i]
        return -1
        
