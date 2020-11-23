# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        TreeCache = {}
        
        def cacheTree(node):
            nonlocal TreeCache
            TreeCache[id(node)] = node
            if node.left:
                cacheTree(node.left)
            if node.right:
                cacheTree(node.right)
                
        @lru_cache(maxsize=None)
        def getHaul(nodeid, skip):
            nonlocal TreeCache
            node = TreeCache[nodeid]
            val = 0
            if not skip:
                val = node.val
                
            if node.left:
                if skip:
                    val += max(getHaul(id(node.left), not skip), getHaul(id(node.left), skip))
                else:
                    val += getHaul(id(node.left), not skip)
                
                
            if node.right:
                if skip:
                    val += max(getHaul(id(node.right), not skip), getHaul(id(node.right), skip))
                else:
                    val += getHaul(id(node.right), not skip)
            
            return val
        
        if root == None:
            return 0
        
        cacheTree(root)
        return max(getHaul(id(root), True), getHaul(id(root), False))
    