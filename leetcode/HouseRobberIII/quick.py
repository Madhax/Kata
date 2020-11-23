
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def sub_rob(node):
            if not node:
                return (0, 0)
            l_child, l_grand_child = sub_rob(node.left)
            r_child, r_grand_child = sub_rob(node.right)
            
            child_profit =  l_child + r_child
            grand_profit = node.val + l_grand_child + r_grand_child
            node_profit = max(child_profit, grand_profit)
            return (node_profit, l_child + r_child)
        return max(sub_rob(root))
            
            
            