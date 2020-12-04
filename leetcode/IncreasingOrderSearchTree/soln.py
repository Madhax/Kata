# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = {}
        nodeIndices = []
        
        def unwrap(node):
            nonlocal nodes, nodeIndices
            nodeIndices.append(node.val)
            nodes[node.val] = node
            if node.left:
                unwrap(node.left)
            if node.right:
                unwrap(node.right)
                
            node.left = None
            
        unwrap(root)
        nodeIndices.sort()
        head = nodes[nodeIndices[0]]
        node = head
        for x in range(1, len(nodeIndices)):
            node.right = nodes[nodeIndices[x]]
            node = node.right
        
        node.right = None
        
        return head
            