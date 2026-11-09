class SegmentTreeNode:

    def __init__(self, total: int, L: int, R: int):
        self.sum_total = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        # base case
        # leaf node, single value at L
        if L == R:
            return SegmentTreeNode(nums[L], L, R)

        # midpoint, round down with integer division
        M = (L + R) // 2

        # build left and right partitioned by midpoint
        root = SegmentTreeNode(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)

        # update sum total
        root.sum_total = root.left.sum_total + root.right.sum_total

        return root
    
    def update(self, index: int, val: int) -> None:
        self._update(self.root, index, val)

    def _update(self, root, index, val):
        # base case
        # leaf node, single value at L
        if root.L == root.R:
            root.sum_total = val
            return

        # midpoint
        M = (root.L + root.R) // 2

        # update left tree
        if index <= M:
            self._update(root.left, index, val)
        # update right tree
        else:
            self._update(root.right, index, val)

        # update sum total
        root.sum_total = root.left.sum_total + root.right.sum_total
    
    def query(self, L: int, R: int) -> int:
        return self._query(self.root, L, R)

    def _query(self, root, L, R):
        # base case, node matches L and R
        if L <= root.L and root.R <= R:
            return root.sum_total

        # L or R are out of bounds
        if L > root.R or R < root.L:
            return 0

        # query left and right trees
        return self._query(root.left, L, R) + self._query(root.right, L, R)