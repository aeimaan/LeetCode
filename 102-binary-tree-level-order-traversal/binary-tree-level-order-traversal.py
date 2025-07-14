# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        level = []
        level.append(root)

        while level:
            tmp = []
            for i in range(len(level)):
                node = level.pop(0)
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
        return res
            
        