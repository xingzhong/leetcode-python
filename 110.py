# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def checkHeight(self, root):
        if root is None: return 0
        lh = self.checkHeight(root.left)
        if lh == -1: return -1
        rh = self.checkHeight(root.right)
        if rh == -1: return -1
        if abs( lh - rh ) > 1:
            return -1
        else:
            return 1 + max(lh, rh)
            
    def isBalanced(self, root):
        return self.checkHeight(root) != -1
