

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def hasNode(node, cond):
            if not node:
                return False
            
            if node == cond:
                return True
            
            if node.left and hasNode(node.left, cond):
                return True
            
            if node.right and hasNode(node.right, cond):
                return True
            
            return False
        
        def LCA(node):
            if not node:
                return False
            
            ret = LCA(node.left)
            if ret:
                return ret
            
            ret = LCA(node.right)
            if ret:
                return ret
            
            if hasNode(node, p) and hasNode(node, q):
                return node
            
            return False
        
        ret = LCA(root)
        #print(ret)
        return ret
                