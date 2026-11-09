class Solution:
    # Backtracking
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(i, curr, total):
            # total matches target, add to result
            if total == target:
                # copy curr since modified
                result.append(curr.copy())
                return

            # out of bounds or exceeds target
            if i >= len(nums) or total > target:
                return

            # with candidate num
            curr.append(nums[i])
            backtrack(i, curr, total + nums[i])
            # without candidate num
            curr.pop()
            backtrack(i + 1, curr, total)

        backtrack(0, [], 0)

        return result