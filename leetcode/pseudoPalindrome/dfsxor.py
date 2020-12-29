# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        # Find all the paths
        # Use xor to decide if the given path is pseudo-palindromic
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    
    def dfs(self, node, x):
        y = x ^ (1<<node.val)
        if not node.left and not node.right:
            if y & (y-1) == 0:
                self.ans += 1
        else:
            if node.left:
                self.dfs(node.left, y)
            if node.right:
                self.dfs(node.right, y)