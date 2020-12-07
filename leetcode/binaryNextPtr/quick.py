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
        if root is None:
            return root
        
        queue = collections.deque()
        queue.append(root)
        while queue:
            length = len(queue)
            pre = None
            for _ in range(length):
                node = queue.popleft()
                if pre is not None:
                    pre.next = node
                pre = node
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                    
        return root