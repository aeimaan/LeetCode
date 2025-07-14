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
            nonlocal res
            if not node: return
            if node.val == lo or node.val == hi:
                res = node
                return
            elif lo < node.val and node.val < hi:
                res = node
                return
            dfs(node.left, lo, hi)
            dfs(node.right, lo, hi)
        dfs(root,lo,hi)
        return res
            