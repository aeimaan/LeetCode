# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, hi):
            if not node: return 0
            left = dfs(node.left, max(hi, node.val))
            right = dfs(node.right, max(hi, node.val))

            count = 0
            if node.val >= hi: count += 1
            return left + right + count
        return dfs(root, root.val)