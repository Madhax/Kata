# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        curr_level = [root]
        rst = []
        while len(curr_level) > 0:
            rst.append(curr_level[-1].val)
            next_level = []
            for n in curr_level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            
            curr_level = next_level
        
        return rst