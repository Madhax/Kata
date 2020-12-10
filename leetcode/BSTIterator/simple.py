# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.s = []
        
        while root:
            self.s.append(root)
            root = root.left

    def next(self) -> int:
        
        itm = self.s.pop()
        
        nxt = itm.right
        
        while nxt:
            self.s.append(nxt)
            nxt = nxt.left
            
        return itm.val
        
    def hasNext(self) -> bool:
        return len(self.s) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()