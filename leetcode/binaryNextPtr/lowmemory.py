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
        # current level is already connected
        # next_head, prev, 
        # left, right if not None: prev -> child and update the prev
        
        node = root
        next_head, prev = None, None
        while node:
            for child in (node.left, node.right):
                if child:
                    if not next_head:
                        next_head = child
                    if prev:
                        prev.next = child
                    prev = child
            node = node.next
            if not node:
                node = next_head
                next_head, prev = None, None
        
        return root
