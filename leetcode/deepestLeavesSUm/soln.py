# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        d = defaultdict(list)
        
        
        def recurse(level, node):
            d[level].append(node.val)
            
            if node.left:
                recurse(level+1, node.left)
                
            if node.right:
                recurse(level+1, node.right)
                
        recurse(0, root)
        #print(d.keys())
        #return 0
        return sum(d[max(d.keys())])