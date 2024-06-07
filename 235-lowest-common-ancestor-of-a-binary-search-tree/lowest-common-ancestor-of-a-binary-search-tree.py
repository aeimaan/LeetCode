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

        p,q = min(p.val,q.val), max(p.val,q.val)
        last_parent = root

        def recurse(node):
            nonlocal last_parent
            last_parent = node
            if node.val > p and node.val > q:
                recurse(node.left)
            elif node.val < p and node.val < q:
                recurse(node.right)
            else:
                return
        
        recurse(root)
        return last_parent
