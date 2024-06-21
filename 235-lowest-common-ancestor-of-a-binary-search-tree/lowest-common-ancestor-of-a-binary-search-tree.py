# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # BST the left node < root Node < right Node
        # So the common ancestor has to be where the min(p,q) falls on left or root and the max else

        p, q = min(p.val, q.val), max(p.val, q.val)

        def dfs(node, p, q):
            if node.val > p and node.val > q:
                return dfs(node.left, p, q)
            elif node.val < p and node.val < q:
                return dfs(node.right, p, q)
            else:
                return node
            
        return dfs(root, p, q)
