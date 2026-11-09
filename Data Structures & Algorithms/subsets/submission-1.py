class Solution:
    # Backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        # visit each node with in-order traversal
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # include num and explore
            subset.append(nums[i])
            dfs(i + 1)

            # exclude num and explore
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result