# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
       
        d = defaultdict(lambda: [0,0])
       
        def recurse(level, node):
           
            d[level][0] += 1
            d[level][1] += node.val
           
            if node.left:
                recurse(level+1, node.left)
            if node.right:
                recurse(level+1, node.right)
           
        recurse(0, root)
       
        output = []
        #keys = [d.keys()]
        #keys.sort()
        #print(keys)
        for key in d.keys():
            #print(key, d[key])
            output.append(d[key][1]/d[key][0])
           
        return output
