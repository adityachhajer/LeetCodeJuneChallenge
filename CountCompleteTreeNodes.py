# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        x = 0
        d = [root]
        while d:
            c = []
            for i in d:
                x = x + 1
                if i.left:
                    c.append(i.left)
                if i.right:
                    c.append(i.right)
            d = c
        return x
