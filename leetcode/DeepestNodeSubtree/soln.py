# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        d = {}
        nodes = {}
        maxDepth = 0
        def recurseBST(node, parents, depth):
            nonlocal d, maxDepth
            if depth > maxDepth:
                maxDepth = depth
                
            if depth not in d:
                d[depth] = [[node]]
            else:
                d[depth].append([node])
                
            
            parents.add(node.val)
            nodes[id(node)] = [node, parents.copy()]
            
            
            
            if node.left:
                recurseBST(node.left, parents, depth+1)
            if node.right:
                recurseBST(node.right, parents, depth+1)
            
            parents.remove(node.val)
        
        #find deepest, then find common parent between two
        
        recurseBST(root, set(), 0)
        
        deepestLeafs = [x[0] for x in d[maxDepth]]
        #print(deepestLeafs)
        #print(len(d[maxDepth]), d[maxDepth][0][0].val, d[maxDepth][1][0].val )
        
        #common parents
        commonParents = nodes[id(deepestLeafs[0])][1]
        for leaf in deepestLeafs:
            commonParents = commonParents.intersection(nodes[id(leaf)][1])
            
        
        #print(commonParents)
        bestNode = None
        bestScore = float("inf")
        for nodeid in nodes.keys():
            #find smallest one that has all subset
            
            if commonParents.issubset(nodes[nodeid][1]):
                if len(nodes[nodeid][1]) < bestScore:
                    bestNode = nodes[nodeid][0]
                    bestScore = len(nodes[nodeid][1])
                
        return bestNode
        
        #return d[maxDepth][0]
                
            