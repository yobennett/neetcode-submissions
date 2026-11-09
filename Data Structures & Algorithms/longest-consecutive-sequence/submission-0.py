class Solution:
    # UnionFind
    def longestConsecutive(self, nums: List[int]) -> int:
        # sanity check
        if not nums:
            return 0

        # initialize
        parent = {}
        size = {}
        for i in set(nums):
            parent[i] = i
            size[i] = 1

        def find(n):
            if n != parent[n]:
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1, n2):
            root1, root2 = find(n1), find(n2)
            if root1 == root2:
                return size[root1]

            if size[root1] < size[root2]:
                root1, root2 = root2, root1
            
            parent[root2] = root1
            size[root1] += size[root2]

            return size[root1]

        result = 1

        for n in parent:
            if n + 1 in parent:
                result = max(result, union(n, n + 1))

        return result
