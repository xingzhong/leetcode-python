# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        
        def isbst(root):
            if root is None : return True
            rrange = isbst(root.right)
            lrange = isbst(root.left)
            if rrange is False or lrange is False:
                return False
            if (lrange is True or root.val > lrange[1]) and (rrange is True or root.val < rrange[0]):
                return (root.val if lrange is True else lrange[0], 
                        root.val if rrange is True else rrange[1])
            else:
                return False
        
        return isbst(root) is not False
