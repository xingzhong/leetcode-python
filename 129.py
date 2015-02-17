# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None : return 0
        
        def path(root):
            if root is None : return []
            if not (root.left or root.right):
                return [(root.val, 0)]
            res = []
            for p, n in path(root.left):
                res.append((root.val * 10 ** (n+1) + p, n+1))
            for p, n in path(root.right):
                res.append((root.val * 10 ** (n+1) + p, n+1))
            return res
        
        return sum(map(lambda x:x[0], path(root)))
            
