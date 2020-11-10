# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
       
        maxDiff = 0
        def traverse(node, lowest, highest):
            nonlocal maxDiff
            ldiff, hdiff = abs(lowest-node.val), abs(highest-node.val)
            if ldiff > maxDiff:
                maxDiff = ldiff
            elif hdiff > maxDiff:
                maxDiff = hdiff
               
            if node.right:
                traverse(node.right, min(lowest, node.val), max(highest, node.val))
            if node.left:
                traverse(node.left, min(lowest, node.val), max(highest, node.val))
       
        traverse(root, root.val, root.val)
        return maxDiff
