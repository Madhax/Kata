# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def isEqual(node1, node2):
            if node1.val != node2.val:
                return False
            
            retVal = True
            
            try:
                if node1.left:
                    retVal |= isEqual(node1.left, node2.left)
                    
                if node1.right and retVal:
                    retVal |= isEqual(node1.right, node2.right)
                
            except:
                return False
            
            return retVal
        
        def find(node, nodeToFind):
            
            if isEqual(node, nodeToFind):
                return node
            
            if node.left:
                retVal = find(node.left, nodeToFind)
                if retVal is not None:
                    return retVal
                
            if node.right:
                retVal = find(node.right, nodeToFind)
                if retVal is not None:
                    return retVal
            
            return None
            
        return find(cloned, target)
        