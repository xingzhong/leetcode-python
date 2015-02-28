# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothin
    def connect(self, root):
        if root is None :
            return
        queue = [root]
        while len(queue) > 0 :
            nq = []
            prev = None
            for node in queue[1:] :
                if prev: prev.next = node
                prev = node
                if node.left : nq.append(node.left)
                if node.right : nq.append(node.right)
            queue = nq
        
                
