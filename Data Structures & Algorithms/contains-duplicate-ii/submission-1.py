class Solution:
    # sliding window
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            # NeetCode explanation video is incorrect, has an off-by-one bug
            # (R - L) + 1 > k
            if (R - L) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])

        return False