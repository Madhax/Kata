# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countNodes(node, maxVal):
            if node is None:
                return 0
            
            if node.left == None and node.right == None:
                return 1 if maxVal <= node.val else 0
            
            cnt = 1 if node.val >= maxVal else 0
            
            if node.left:
                cnt += countNodes(node.left, max(node.val, maxVal))
                
            if node.right:
                cnt += countNodes(node.right, max(node.val, maxVal))
                
            return cnt
        
        return countNodes(root, -math.inf)