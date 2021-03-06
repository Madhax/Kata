# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        queue = [root]
        answer = []
        
        while queue:
            temp = []
            answer.append(self.Average(queue))

            for el in queue:
                if el.left != None:
                    temp.append(el.left)
                if el.right != None:
                    temp.append(el.right)
            queue = temp
    
        return answer
    
    def Average(self, queue):
        total = 0
        n = 0

        for el in queue:
            total += el.val
            n += 1

        return float(total/n)
        
                