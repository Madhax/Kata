# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        if not root:
            if len(voyage)==0: return True
            return False
        
        res = []
        i = 0
        def helper(node):
            nonlocal i
            if node is None and i<len(voyage):
                return False
            if node.val != voyage[i]:
                return False
            i += 1
            swapped = False
            if node.left:
                if node.left.val != voyage[i]:
                    res.append(node.val)
                    temp = node.left
                    node.left = node.right
                    node.right = temp
                    swapped = True
                left_res = helper(node.left)
            else:
                left_res = True
            
            if node.right:
                if node.right.val != voyage[i]:
                    right_res = False
                right_res = helper(node.right)
            else:
                right_res = True
            # print("node", node.val)
            # if node.left:
            #     print("node.left", node.left.val)
            # if node.right:
            #     print("node.right", node.right.val)
            return left_res and right_res
        
        
        # print(helper(root))
        flag = helper(root)
        if not flag: 
            return [-1]
        return res
                    