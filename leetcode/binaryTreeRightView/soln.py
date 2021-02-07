from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        d = defaultdict(list)
        def recurse(node, depth):
            nonlocal d
            if node is None:
                return
            d[depth].append(node.val)
            if node.left:
                recurse(node.left, depth+1)
            if node.right:
                recurse(node.right, depth+1)
            
                
        recurse(root, 0)
        return [d[x][-1] for x in d.keys() if len(d[x]) > 0]