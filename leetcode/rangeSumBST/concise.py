# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        def dfs(head):
            if  head : 
                if L <= head.val <= R:
                    self.ans +=head.val 
                if L <head.val :
                    dfs(head.left)
                if head.val <R :
                    dfs(head.right)
        dfs(root)
        return self.ans
