# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lo = min(p.val, q.val)
        hi = max(p.val, q.val)
        res = root
        def dfs(node, lo, hi):
            if node.val < lo and node.val < hi:
                return dfs(node.right,lo,hi)
            elif node.val > lo and node.val > hi:
                return dfs(node.left, lo,hi)
            else:
                return node
        return dfs(root, lo,hi)
            