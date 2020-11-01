# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = []
        self.addLeftNodes(stack, root)
        prev = None
        swapNodes = [None, None]
        
        while stack:
            node = stack.pop()
            if prev and node.val < prev.val:
                swapNodes[0] = node
                if swapNodes[1] is None:
                    swapNodes[1] = prev
                else:
                    break
            prev = node
            self.addLeftNodes(stack, node.right)
        
        swapNodes[0].val, swapNodes[1].val = swapNodes[1].val, swapNodes[0].val
            
        
    
    def addLeftNodes(self, stack, root):
        while root:
            stack.append(root)
            root = root.left