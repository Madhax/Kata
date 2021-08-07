"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        d = defaultdict(list)
        
        def recurse(level, node):
            
            d[level].append(node.val)
            for child in node.children:
                recurse(level+1, child)
                

        if root == None:
            return []
        recurse(0, root)
        return [d[child] for child in sorted(d.keys())]
    
        
        