# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        def traverse(node, x, y):
            nonlocal d
            d[x].append((y, node.val))
            if node.left:
                traverse(node.left, x-1, y-1)
            if node.right:
                traverse(node.right, x+1, y-1)
       
        traverse(root, 0, 0)
        output = []
        for x in sorted(d.keys()):
            d[x].sort(key=lambda x: ((abs(x[0])+1)*1000)+x[1])
            entry = []
            for val in d[x]:
                entry.append(val[1])
               
            output.append(entry)
       
        return output