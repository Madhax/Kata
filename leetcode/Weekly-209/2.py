from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a = defaultdict(list)
        def _dfs(u, d):
            if not u: return
            a[d].append(u.val)
            _dfs(u.left, d+1)
            _dfs(u.right, d+1)
        _dfs(root, 0)
        for k, v in a.iteritems():
            if any((i&1) == (k&1) for i in v):
                return False
            if k & 1: v.reverse()
            if any(v[i] <= v[i-1] for i in xrange(1, len(v))):
                return False
        return True
        
