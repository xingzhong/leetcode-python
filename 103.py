# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None : return []
        queue = [root]
        res = []
        flag = False
        while len(queue) > 0 :
            nq = []
            r = []
            for node in queue :
                r.append(node.val)
                if node.left : nq.append(node.left)
                if node.right : nq.append(node.right)
            if flag :
                res.append(r[::-1])
                flag = False
            else:
                res.append(r)
                flag = True
            queue = nq
        return res
