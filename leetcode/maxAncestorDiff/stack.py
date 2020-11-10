# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        # self.res = 0
        # cur_min = float("inf")
        # cur_max = float("-inf")
        # def dfsTopDown(node, cur_min, cur_max):
        #     if node:
        #         # udpate res
        #         self.res = max(self.res, abs(node.val-cur_max), abs(node.val-cur_min))
        #         # update max, min
        #         cur_min = min(node.val, cur_min)
        #         cur_max = max(node.val, cur_max)
        #         dfsTopDown(node.left, cur_min, cur_max)
        #         dfsTopDown(node.right, cur_min, cur_max)
        # dfsTopDown(root, root.val, root.val)
        # return self.res
        
        stack = [(root, root.val, root.val)]
        res = float('-inf')
        
        while stack:
            node, parent_max, parent_min = stack.pop()
            res = max([res, abs(parent_max - node.val), abs(parent_min - node.val)])
            parent_max = max(parent_max, node.val)
            parent_min = min(parent_min, node.val)
            if node.left:
                stack.append((node.left, parent_max, parent_min))
            if node.right:
                stack.append((node.right, parent_max, parent_min))
        
        return res
        