# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.numCam = 0
        self.covered = {None}
        
    def dfs(self, node, par = None):
        if node:
            self.dfs(node.left, node)
            self.dfs(node.right, node)
            
            if((par is None and node not in self.covered) or (node.left not in self.covered or node.right not in self.covered)):
                self.numCam += 1
                self.covered.update({node, node.left, node.right, par})
                
        return
        
    
    def minCameraCover(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        self.dfs(root, None)
        
        return self.numCam
        