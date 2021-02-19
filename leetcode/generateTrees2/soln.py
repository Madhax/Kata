# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        
        def helper(cand):
            
            if len(cand) == 0:
                return [None]
            
            
            output = []
            for root in cand:
                leftTree = helper([x for x in cand if x < root])
                rightTree = helper([x for x in cand if x > root])
                
                
                #output += [TreeNode(val=root, left=l, right=r) for l in leftTree for r in rightTree]
                
                
                for l in leftTree:
                    for r in rightTree:
                        #t = TreeNode(root, l, r)
                        t = TreeNode(root)
                        t.left = l
                        t.right = r
                        output.append(t)
                
            return output
            
        
        
        #l = [1,2,3]
        #r = [10, 11, 12]
        
        #print([[x, y] for x in l for y in r])
        return helper([x for x in range(1, n+1)])