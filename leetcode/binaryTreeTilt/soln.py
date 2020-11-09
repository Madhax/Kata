# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sumMemo = {}
    def findTilt(self, root: TreeNode) -> int:
        self.sumMemo = {}
        
        def tiltOf(node):
            if node is None:
                return 0
            return abs(sumOf(node.left) - sumOf(node.right))
        
        def sumOf(node):
            if node == None:
                return 0
            
            if node is None:
                return 0
            
            if id(node) in self.sumMemo:
                return self.sumMemo[id(node)]
                
            retVal = node.val + sumOf(node.left) + sumOf(node.right)
            self.sumMemo[id(node)] = retVal
            return retVal
        
        def sumOfTilt(node):
            if node is None:
                return 0
            
            return tiltOf(node) + sumOfTilt(node.left) + sumOfTilt(node.right)
        
        return sumOfTilt(root)