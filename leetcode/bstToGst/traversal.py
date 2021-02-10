# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    preSum = 0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return 0
            
            if node.right:
                self.preSum = dfs(node.right)
            
            node.val += self.preSum
            self.preSum = node.val
            
            if node.left:
                self.preSum = dfs(node.left)
            
            return self.preSum
        
        dfs(root)
        
        return root
                        