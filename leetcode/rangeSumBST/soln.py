# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
       
        def recurseBST(node, low, high):
            if node == None:
                return 0
           
            value = 0
            if node.val >= low and node.val <= high:
                value = node.val
               
            value += recurseBST(node.left, low, high)
            value += recurseBST(node.right, low, high)
           
            return value
       
        return recurseBST(root, low, high)