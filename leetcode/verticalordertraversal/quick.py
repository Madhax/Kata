# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        grid = {}
        queue = [(root, 0, 0)]
        res = []
        for cur in queue:
            if cur[0]:
                horizon, lvl = cur[1], cur[2]
                if not cur[1] in grid:
                    grid[cur[1]]=[[lvl, cur[0].val]]
                else:
                    grid[cur[1]].append([lvl, cur[0].val])
                queue.append((cur[0].left, horizon-1, lvl+1))
                queue.append((cur[0].right, horizon+1, lvl+1))
        for i in sorted(grid.keys()):
            # print("i:",i)
            # print("grid[i]:",grid[i])
            res.append([value[1] for value in sorted(grid[i])])
        return res
                        
        