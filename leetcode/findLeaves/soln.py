# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        output = []
        
        def isLeaf(node):
            return node.left == None and node.right == None
            
        def recurse(node):
            if node == None:
                return
            
            if node.left and isLeaf(node.left):
                output[-1].append(node.left.val)
                node.left = None
                
            else:
                recurse(node.left)
                
            if node.right and isLeaf(node.right):
                output[-1].append(node.right.val)
                node.right = None
            else:
                recurse(node.right)
                
            return
        
        while not isLeaf(root):
            output.append([])
            recurse(root)
            
        output.append([root.val])
        return output
    