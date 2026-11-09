class Solution:
    # bucket/counting sort
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3 # possible colors: 0, 1, 2
        for num in nums:
            counts[num] += 1

        i = 0 # write pointer
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1
