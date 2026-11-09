class Solution:
    # Backtracking
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(pos, c):
            # return if k numbers chosen
            if len(c) == k:
                # copy combination since mutated later
                result.append(c.copy())
                return

            # iterate through remaining nums
            for i in range(pos, n + 1):
                # add to combination
                c.append(i)
                # explore next remaining num
                backtrack(i + 1, c)
                # cleanup
                c.pop()

        backtrack(1, [])

        return result