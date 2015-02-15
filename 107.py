# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root is None : return []
        level = [root]
        res = []
        while len(level) > 0 :
            tlevel = []
            r = []
            for node in level :
                r.append(node.val)
                if node.left: tlevel.append(node.left)
                if node.right: tlevel.append(node.right)
            level = tlevel
            res.append(r)
        return res[::-1]
