# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    node1 = None
    node2 = None
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        self.node1 = None
        self.node2 = None
        
        def inOrder(node):
            if node == None:
                return
            
            inOrder(node.left)
            
            if self.prev != None and self.prev.val > node.val:
                if self.node1 == None:
                    self.node1 = self.prev
                    
                self.node2 = node
                #print(node)
            
            self.prev = node
            inOrder(node.right)
            
        inOrder(root)
        tmp = self.node2.val
        self.node2.val = self.node1.val
        self.node1.val = tmp
        return
    
            