# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        
        d = defaultdict(list)
        
        def recurse(node, level):
            d[level].append(node.val)
            
            if node.left:
                recurse(node.left, level+1)
            if node.right:
                recurse(node.right, level+1)
        
        recurse(root, 1)
        
        output = []
        for key in sorted(d.keys()):
            output.append(d[key])
            
        return output
        