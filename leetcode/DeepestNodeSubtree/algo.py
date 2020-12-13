# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        parent = {root: None}
        
        curr = [root]
        prev = []
        
        while curr:
            prev = curr
            curr = []
            for n in prev:
                for c in [n.left, n.right]:
                    if c:
                        curr.append(c)
                        parent[c] = n
        
        res = set(prev)
        
        while len(res) > 1:
            res = set([parent[n] for n in res])
            
        return list(res)[0]
        
