# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if not (p and q): return not (p or q)
        return all( [p.val == q.val,  self.isSameTree(p.left, q.left),
                self.isSameTree(p.right, q.right) ])
