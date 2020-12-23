# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution(object):
    def helper(self, root):
        if root == None:
            return 0, True
        hl, lb = self.helper(root.left)
        hr, rb = self.helper(root.right)
        if lb and rb and abs(hl-hr) <= 1:
            return max(hl,hr) + 1, True
        else:
            return -1, False

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        h, is_b = self.helper(root)
        return is_b