"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        if root is None:
            return None
       
        def traverse(node):
            output.append(node.val)
            for child in  node.children:
                traverse(child)
               
        traverse(root)
        return output
