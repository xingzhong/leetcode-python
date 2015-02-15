# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None : return True
        queue = [root]
        while len(queue)>0:
            level, nq = [], []
            for node in queue:
                if node:
                    level.append(node.val)
                    nq.append(node.left)
                    nq.append(node.right)
                else:
                    level.append(None)
            for i in range(len(level)/2):
                if level[i] != level[-1-i]:
                    return False
            queue = nq
        return True
