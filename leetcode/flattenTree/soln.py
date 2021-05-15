# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        arr = []
        
        def recurse(node):
            arr.append(node.val)
            if node.left:
                recurse(node.left)
            if node.right:
                recurse(node.right)
                
        recurse(root)
        
        output = root
        curnode = output
        
        for x in range(len(arr)):
            curnode.val = arr[x]
            curnode.left = None
            if x < len(arr) - 1:
                curnode.right = TreeNode()
                curnode = curnode.right
        #print(output)
        #return output
        