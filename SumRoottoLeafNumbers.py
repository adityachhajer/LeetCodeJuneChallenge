# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, s, l):
        if root is None:
            return
        if root.left is None and root.right is None:
            s = s + str(root.val)
            l.append(int(s))
            print(l)
        s = s + str(root.val)
        if root.left:
            self.solve(root.left, s, l)
        if root.right:
            self.solve(root.right, s, l)

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root and root.left is None and root.right is None:
            return root.val
        l = []
        s = ''
        self.solve(root, s, l)
        return sum(l)
