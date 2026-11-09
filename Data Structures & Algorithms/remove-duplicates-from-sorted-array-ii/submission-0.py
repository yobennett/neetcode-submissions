class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0

        while R < len(nums):
            count = 1

            # advance R while R == R + 1
            # track count
            while R + 1 < len(nums) and nums[R] == nums[R + 1]:
                R += 1
                count += 1

            # write at most 2 at L
            # advance L per write
            for i in range(min(2, count)):
                nums[L] = nums[R]
                L += 1
            
            # advance R
            R += 1

        return L