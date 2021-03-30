# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        output = []
        index = 0
        def preOrder(node):
            nonlocal voyage, output, index
            if index == len(voyage):
                output = [-1]
                return False
            
            if node and node.val != voyage[index]:
                output = [-1]
                return False
            elif node is None and voyage[index] != None:
                output = [-1]
                return False
            #print(node.val)
            index += 1
            
            if node.left:
                if index == len(voyage):
                    output = [-1]
                    return False
                
                if node.left.val != voyage[index]:
                    node.left, node.right = node.right, node.left
                    output.append(node.val)
                if preOrder(node.left) == False:
                    return False
            
            if node.right:
                if index == len(voyage):
                    output = [-1]
                    return False
                
                if node.right.val != voyage[index]:
                    node.left, node.right = node.right, node.left
                    output.append(node.val)
                    
                if preOrder(node.right) == False:
                    return False
                
            
        preOrder(root)
        return output