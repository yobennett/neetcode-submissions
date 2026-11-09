"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(node):
            if node in cloned:
                return cloned[node]

            clone  = Node(node.val)
            cloned[node] = clone
            for neighbor in node.neighbors:
                neighborClone = dfs(neighbor)
                clone.neighbors.append(neighborClone)
            return clone

        return dfs(node) if node else None
