# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []

        if root: q.append(root)


        while q: 
            level = []
            for i in range(len(q)):
                cur = q.pop(0)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
                level.append(cur.val)
            res.append(level[-1])

        return res