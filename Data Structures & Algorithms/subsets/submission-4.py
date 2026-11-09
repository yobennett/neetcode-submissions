class Solution:
    # Backtracking + Subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs(i):
            # out of bounds
            if i == len(nums):
                # copy since subset is modified
                results.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return results