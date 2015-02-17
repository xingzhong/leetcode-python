# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None : return None
        root = UndirectedGraphNode(node.label)
        hmap = {node : root}
        queue = [node]
        while len(queue) > 0 :
            n = queue.pop()
            for nbr in n.neighbors:
                if nbr not in hmap:
                    hmap[nbr] = UndirectedGraphNode(nbr.label)
                    queue.append(nbr)
                hmap[n].neighbors.append(hmap[nbr])
                
        return root
