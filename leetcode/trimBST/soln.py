# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
       
        def getValidNode(node):
            nonlocal low, high
           
            if node is None:
                return node
           
            if node.val > high:
                return getValidNode(node.left)
       
            elif node.val < low:
                return getValidNode(node.right)
           
            if node.left:
                node.left = getValidNode(node.left)
               
            if node.right:
                node.right = getValidNode(node.right)
               
            return node
       
       
        return getValidNode(root)