# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        output = []
        
        def recurse(node, l, s):
            if node == None:
                return
            if node.left == None and node.right == None and s == 0:
                output.append(l.copy())
                
            if node.left:
                l.append(node.left.val)
                recurse(node.left, l, s-node.left.val)
                l.pop()
                
            if node.right:
                l.append(node.right.val)
                recurse(node.right, l, s-node.right.val)
                l.pop()
                
            
        if root:
            recurse(root, [root.val], targetSum-root.val)
        return output
    