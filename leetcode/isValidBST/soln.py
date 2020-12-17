# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def isValid(node, lower, upper):
            if lower >= node.val:        
                return False
            
            if upper <= node.val:
                return False
                
            ret = True
            if node.right:
                ret = ret and isValid(node.right, node.val, upper)
            
            if node.left and ret:
                ret = ret and isValid(node.left, lower, node.val)
                
            return ret
        
        return isValid(root, float("-inf"), float("inf"))