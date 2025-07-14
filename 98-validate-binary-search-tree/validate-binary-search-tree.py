# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        when we go left, the root is the max
        when we go right, the root is the min
        '''

        def dfs(lo, node, hi):
            if not node: return True
            if (node.val <= lo) or (node.val >= hi):
                return False
            return dfs(lo, node.left, node.val) and dfs(node.val, node.right, hi)
        return dfs(-99999999999, root, 99999999999)
