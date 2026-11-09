class Solution:
    # backtracking with hash map
    # complexity
    #   time O(n! * n)
    #       n! permutations
    #       explore n times
    #   space O(n! * n)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        perm = []

        count = {n:0 for n in nums}
        for num in nums:
            count[num] += 1

        def dfs():
            # base case, full permutation
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            # iterate through count hashmap
            for num in count:
                # only consider nums where remaining count is positive
                if count[num] > 0:
                        # choose num, decrement count
                        perm.append(num)
                        count[num] -= 1

                        # explore num
                        dfs()

                        # backtrack undo num, increment count
                        perm.pop()
                        count[num] += 1

        dfs()
        return result