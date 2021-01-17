# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target):
        if root is None:
            return False
        if root.val == target:
            return True
        else:
            return self.solve(root.left, target) | self.solve(root.right, target)
