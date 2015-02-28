# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None : return []
        if not (root.left or root.right):
            if root.val == sum : 
                return [[root.val]]
            else:
                return []
            
        res = []
        t = sum - root.val
        for path in self.pathSum(root.left, t):
            res.append([root.val] + path)
        for path in self.pathSum(root.right, t):
            res.append([root.val] + path) 
        
        return res
