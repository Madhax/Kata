"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        maxLevel = 0
        nodes = {}
        def traverse(node, level):
            nonlocal nodes, maxLevel
            if level > maxLevel:
                maxLevel = level
            if level not in nodes:
                nodes[level] = [node]
            else:
                nodes[level].append(node)
               
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
               
        traverse(root, 0)
        for level in range(maxLevel+1):
            for nodeiter in range(0, len(nodes[level])-1):
                #print(level, maxLevel, nodes[2][2].val)
                #print(nodes[level][nodeiter].val, "to", nodes[level][nodeiter+1].val)
                nodes[level][nodeiter].next = nodes[level][nodeiter+1]
               
        return root
