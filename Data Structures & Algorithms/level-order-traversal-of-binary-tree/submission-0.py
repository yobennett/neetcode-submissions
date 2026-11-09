# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        result = []

        queue.append(root)
        level = 0

        while queue:
            nodes = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    nodes.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if nodes:
                result.append(nodes)
            level += 1

        return result