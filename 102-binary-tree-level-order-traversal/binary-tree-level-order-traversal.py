# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = []

        if root: q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                x = q.pop(0)
                if x.left: q.append(x.left)
                if x.right: q.append(x.right)
                level.append(x.val)
            res.append(level)

        return res