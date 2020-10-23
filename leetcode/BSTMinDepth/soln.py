# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        deck = deque()
        depth = 1
        deck.append([root, depth])
        
        while len(deck) > 0:
            node = deck.popleft()
            if node[0].left == None and node[0].right == None:
                return node[1]
            if node[0].left != None:
                deck.append([node[0].left, node[1]+1])
            if node[0].right != None:
                deck.append([node[0].right, node[1]+1])
            
            
        return 0