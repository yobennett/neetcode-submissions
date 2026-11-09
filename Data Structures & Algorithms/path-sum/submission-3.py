# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # BFS
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque()
        queue.append([root, targetSum - root.val])

        while queue:
            item = queue.popleft()
            node = item[0]
            currSum = item[1]
            if not node.left and not node.right and currSum == 0:
                return True
            if node.left:
                queue.append([node.left, currSum - node.left.val])
            if node.right:
                queue.append([node.right, currSum - node.right.val])
        
        return False