# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        foundP = False
        foundQ = False
        pStack = None
        qStack = None
        
        s = []
        
        def findPaths(node):
            nonlocal foundP, foundQ, pStack, qStack
            if node is None:
                return
            s.append((node.val, node))
            if p.val == node.val:
                foundP = True
                pStack = s.copy()
            elif q.val == node.val:
                foundQ = True
                qStack = s.copy()
                
            
            if foundP == False or foundQ == False:
                findPaths(node.left)
                
            if foundP == False or foundQ == False:
                findPaths(node.right)
            
            s.pop()
            
        findPaths(root)
        
        pSet = set([x[0] for x in pStack])
        
        for val, node in reversed(qStack):
            if val in pSet:
                return node
                
            
            