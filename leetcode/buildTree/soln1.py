# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            k=inorder.index(preorder.pop(0))
            root=TreeNode(inorder[k])
            root.left=self.buildTree(preorder,inorder[:k])
            root.right=self.buildTree(preorder,inorder[k+1:])
            return root