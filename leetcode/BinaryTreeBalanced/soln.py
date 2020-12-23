# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
       
        if root == None:
            return True
       
        def recursive(node, level):
            leftHeight = float("-inf")
            rightHeight = float("-inf")
       
               
            if node.right:
                result = recursive(node.right, level+1)
                if result[0] == False:
                    return (False, 0)
               
                rightHeight = max(rightHeight, result[1])
               
               
            else:
                rightHeight = level
               
            if node.left:
                result = recursive(node.left, level+1)
                if result[0] == False:
                    return (False, 0)
               
                leftHeight = max(leftHeight, result[1])
            else:
                leftHeight = level
               
           
            if abs(leftHeight-rightHeight) > 1:
                return (False, max(leftHeight, rightHeight))
           
            return (True, max(leftHeight, rightHeight))
   
        return recursive(root, 0)[0]