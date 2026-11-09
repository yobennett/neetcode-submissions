class Solution:
    # Two pointers
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 1, 1

        while R < len(nums):
            # first time seeing nums[R]
            # increment both L and R 
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
                R += 1
            # duplicate
            # increment R
            else:
                R += 1

        return L        