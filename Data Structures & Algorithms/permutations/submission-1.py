class Solution:
    # Backtracking
    # choose numbers one-by-one and explore all possible orders
    # pick a number not yet used
    # recursively continue building
    # reach base case then return empty array then 
    # insert each num at every possible position 
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(0, nums)
    
    def backtrack(self, i, nums):
        # base case, return empty array as default permutation
        if i == len(nums):
            return [[]]

        result = []

        # DFS for the permutations of the other nums
        permutations = self.backtrack(i + 1, nums)

        # iterate through each permutation
        for perm in permutations:
            # insert nums[i] in each position 
            # before, after (len(perm) + 1) and in between 
            # each of the nums of the permutation
            for j in range(len(perm) + 1):
                permCopy = perm.copy()
                permCopy.insert(j, nums[i])
                result.append(permCopy)

        return result