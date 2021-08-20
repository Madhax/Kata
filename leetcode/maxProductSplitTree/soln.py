# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        best = -math.inf
        total = 0
        
        def countTotal(node):
            ret = node.val
            if node.left:
                ret += countTotal(node.left)
                
            if node.right:
                ret += countTotal(node.right)
                
            return ret
        
        total = countTotal(root)
            
        def recurse(node):
            nonlocal best
            
            left, right = 0, 0
            cur = node.val
            if node.left:
                left = recurse(node.left)
                
            if node.right:
                right = recurse(node.right)
                
            cur += left + right
            
            best = max(best, cur * (total-cur))
            
            return cur
        
        recurse(root)
            
        return best % (10**9 + 7)
            