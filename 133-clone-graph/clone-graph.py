"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        nodeMap = {}

        def dfs(node):
            if node in nodeMap: ## already cloned, ret that clone
                return nodeMap[node] 
            
            # Else clone the node
            clone = Node(node.val)
            nodeMap[node] = clone

            for neighbor in node.neighbors:
                res = dfs(neighbor)
                clone.neighbors.append(res)
            return clone
        
        return dfs(node)