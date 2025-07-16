# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root

        def dfs(node):
            nonlocal res
            if not node: return False
            cur = node.val == p.val or node.val ==q.val
            l = dfs(node.left)
            r = dfs(node.right)
            if (cur) or (l and r):
                res = node
            return (cur) or (l or r)
        dfs(root)
        return res