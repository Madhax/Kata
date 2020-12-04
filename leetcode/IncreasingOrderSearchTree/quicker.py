# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            nonlocal temp
            if not node:
                return

            inorder(node.left)
            temp.right = TreeNode(node.val)
            temp = temp.right
            inorder(node.right)

        result = TreeNode(0)
        temp = result
        inorder(root)

        return result.right