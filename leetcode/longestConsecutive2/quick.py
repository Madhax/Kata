# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        maxpath = 1
        
        def rec(node: TreeNode) -> Tuple[int, int]: 
            
            # TODO: need basecase? 
            inc, dec = 1, 1
            nr, nl = node.right, node.left
            nval = node.val
            
            if nl is not None:
                lval = nl.val
                linc, ldec = rec(nl)
                if nval == lval-1:
                    inc = max(inc, linc+1)
                elif nval == lval+1:
                    dec = max(dec, ldec+1)

            if nr is not None:
                rval = nr.val
                rinc, rdec = rec(nr)
                if nval == rval-1:
                    inc = max(inc, rinc+1)
                elif nval == rval+1:
                    dec = max(dec, rdec+1)
            
            nonlocal maxpath
            maxpath = max(maxpath, (inc+dec-1))
            return inc, dec
        
        rec(root)
        return maxpath