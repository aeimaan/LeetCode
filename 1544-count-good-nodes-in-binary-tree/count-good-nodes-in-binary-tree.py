# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, big):
            if not node:
                return
            val = big
            if node.val >= big:
                nonlocal count
                count += 1
                val = node.val
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, root.val)
        return count