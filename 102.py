# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None : return []
        level, res = [root], []
        while len(level) > 0: 
            r, nl = [], []
            for node in level :
                r.append(node.val)
                if node.left: nl.append(node.left)
                if node.right: nl.append(node.right)
            level = nl
            res.append(r)
        return res
