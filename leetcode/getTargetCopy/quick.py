# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s = [cloned]
        while len(s)>0:
            for i in s:
                if i.val==target.val:
                    return i
                else:
                    if i.left:
                        s.append(i.left)
                    if i.right:
                        s.append(i.right)