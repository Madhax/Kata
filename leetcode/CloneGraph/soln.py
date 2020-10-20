"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    d = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.d = {}
        
        def deepClone(node):
            if node.val in self.d:
                return self.d[node.val]
            
            retNode = Node()
            
            retNode.val = node.val
            retNode.neighbors = []
            
            self.d[retNode.val] = retNode
            
            for nodeIter in node.neighbors:
                retNode.neighbors.append(deepClone(nodeIter))
                
            return retNode
        
        if node is None:
            return node
        
        return deepClone(node)