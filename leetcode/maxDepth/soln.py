# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def recurse(node, level):
            if node.left and node.right:
                return max(recurse(node.left, level+1), recurse(node.right, level+1))
            elif node.left:
                return recurse(node.left, level+1)
            elif node.right:
                return recurse(node.right, level+1)
            else:
                return level
           
        if root == None:
            return 0
        else:
            return recurse(root, 1)