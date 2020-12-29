from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        
        output = 0
        d = defaultdict(int)
        def recurse(node, length, odds):
            nonlocal output, d
            
            
            d[node.val] += 1
            length += 1
            
            if d[node.val] % 2 > 0:
                odds += 1
                
            elif d[node.val] % 2 == 0 and d[node.val] >= 2:
                odds -= 1
                         
            if node.left == None and node.right == None:
                if length%2 == 0 and odds == 0:
                    output += 1
                    
                elif length%2 == 1 and odds == 1:
                    output += 1
                    
            
            if node.left:
                recurse(node.left, length, odds)
                
            if node.right:
                recurse(node.right, length, odds)
                
            d[node.val] -= 1
            
        recurse(root, 0, 0)
        return output
            