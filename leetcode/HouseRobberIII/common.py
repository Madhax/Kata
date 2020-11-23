# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            v1 = root.val + left[1] + right[1]
            v2 = max(left) + max(right)
            return v1,v2
        return max(dfs(root))