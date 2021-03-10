# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        
        def warp(node, level):
            
            if level == d:
                leftnode = TreeNode(v)
                rightnode = TreeNode(v)
                
                leftnode.left = node.left
                rightnode.right = node.right
                
                node.left = leftnode
                node.right = rightnode
                
            else:
                if node.left:
                    warp(node.left, level+1)
                if node.right:
                    warp(node.right, level+1)
                
            return
        
    
        if d == 1:
            head = TreeNode(v)
            head.left = root
            return head
        
        warp(root, 2)
        return root