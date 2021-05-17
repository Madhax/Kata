# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        def recurse(node, isParentCovered, isParentCamera):
            best = math.inf
            print(isParentCovered, isParentCamera)
            if isParentCovered == False:
                cost = 1
                
                if node.left:
                    cost += recurse(node.left, True, True)
                
                if node.right:
                    cost += recurse(node.right, True, True)
                    
                best = min(best, cost)
                
            if isParentCovered == True:
                
                if isParentCamera == True:
                    cost = 0
                
                    if node.left:
                        cost += recurse(node.left, True, False)

                    if node.right:
                        cost += recurse(node.right, True, False)

                    best = min(best, cost)
                    
                else:
                    cost = 0
                
                    if node.left:
                        cost += recurse(node.left, False, False)

                    if node.right:
                        cost += recurse(node.right, False, False)

                    best = min(best, cost)
                    
            if node.left is None and node.right is None and isParentCamera:
                return 0
            if node.left is None and node.right is None and (isParentCovered == False or isParentCamera==False):
                return 1
            
            #print(isParentCovered, isParentCamera, best)
            return best
                
            
            #if isParentCovered == False and isParentCamera == False then cur must be camera
        return recurse(root, True, False)
        #print(recurse(root, False, False), recurse(root, True, False))
        
        #ret = max(min(recurse(root, False, False), recurse(root, True, False)), 1)
        #
        #return ret
        return 0