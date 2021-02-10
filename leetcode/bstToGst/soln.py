# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        vals = []
        
        def recurse(node):
            nonlocal vals
            if node is None:
                return
            
            vals.append(node.val)
            if node.left:
                recurse(node.left)
            if node.right:
                recurse(node.right)
                
        recurse(root)
        vals.sort(reverse=True)
        suffixSum = {}
        
        curSum = 0
        for val in vals:
            suffixSum[val] = curSum
            curSum += val
            
        def build(node):
            nonlocal suffixSum
            if node is None:
                return
            node.val += suffixSum[node.val]
            if node.left:
                build(node.left)
            if node.right:
                build(node.right)
                
        build(root)
        return root
        #vals
        #suffixSum
        