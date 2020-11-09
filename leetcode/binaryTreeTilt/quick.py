# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilt = [0] 
        self.traverse(root, tilt)  
        return tilt[0]
    
    def traverse(self,root, tilt): 
        if (not root):  
            return 0

        left = self.traverse(root.left, tilt)  
        right = self.traverse(root.right, tilt)  
 
        tilt[0] += abs(left - right)  

        return left + right + root.val  
 
