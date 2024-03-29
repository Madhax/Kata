# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        
        def buildBST(nums, l, r):
            if l >= r:
                return None
            
            mid = (l + r) // 2
            
            node = TreeNode(nums[mid])
            node.left = buildBST(nums, l, mid)
            node.right = buildBST(nums, mid+1, r)
            
            return node
        
        return buildBST(nums, 0, len(nums))