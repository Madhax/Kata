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
        """
        tree = dict(level) where it returns array of [val, node ptr]
        populate tree and then recursively fill out next ptr based on current level + value
        """
        tree = {}
        def fillTree(node, level):
            nonlocal tree
            if node == None:
                return
           
            if level in tree:
                tree[level].append([id(node), node])
            else:
                tree[level] = [[id(node), node]]
           
            fillTree(node.left, level+1)
            fillTree(node.right, level+1)
           
        fillTree(root, 1)
           
        def fillNode(node, level):
            nonlocal tree
            if node == None:
                return
           
            nodes = tree[level]
            for index, candidate in enumerate(nodes):
                if candidate[0] == id(node):
                    if index+1 < len(nodes):
                        node.next = nodes[index+1][1]
                    break
           
            fillNode(node.left, level+1)
            fillNode(node.right, level+1)
           
           
        fillNode(root, 1)
        return root