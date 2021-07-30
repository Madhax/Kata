# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
    
        nodeGraph = defaultdict(set)
        nodeCtr = 1
        nodeDict = {}
        
        
        def buildGraph(node, parent):
            nonlocal nodeCtr
            
            nodeDict[nodeCtr] = node
            curNode = nodeCtr
            nodeCtr += 1
            
            if parent is not None:
                nodeGraph[parent].add(curNode)
                nodeGraph[curNode].add(parent)
                
            if node.left:
                buildGraph(node.left, curNode)
            
            if node.right:
                buildGraph(node.right, curNode)
            
        
        buildGraph(root, None)
        seen = set()
        
        @functools.cache
        def getMaxPath(index):
            nonlocal seen
            curVal = nodeDict[index].val
            best = 1
            for node in nodeGraph[index]:
                if node not in seen and nodeDict[node].val == (curVal + 1):
                    seen.add(node)
                    best = max(best, 1 + getMaxPath(node))    
                    seen.remove(node)
            
            return best
                    
        
        best = 0
        #print(getMaxPath(1))
        
        for startNode in range(1, nodeCtr):
            seen.add(startNode)
            best = max(best, getMaxPath(startNode))
            #print(startNode, best)
            seen.remove(startNode)
        
        return best
        