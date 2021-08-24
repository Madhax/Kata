# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        nodeVals = set()
        def recurse(node):
            nonlocal nodeVals
            
            nodeVals.add(node.val)
            
            if node.left:
                recurse(node.left)
                
            if node.right:
                recurse(node.right)
                
            return
        if root:
            recurse(root)
            
        for cand in nodeVals:
            if 2*cand != k and k - cand in nodeVals:
                return True
            
        return False
        
            