class Solution:
    # Backtracking
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        # visit each node with in-order traversal
        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy()) # copy since going to be modified
                return

            # end of bounds or past target total
            if i >= len(nums) or total > target:
                return

            # decision to include nums[i] and explore
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # decision to exclude nums[i] and explore
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return result