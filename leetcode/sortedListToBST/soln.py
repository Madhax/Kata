# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        #if sorted, get median value and use as root and keep using median value for left/right recursively
        
        def getMedian(l, r):
            return (l+r)//2
        
        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        #print(vals)
        def buildSubtree(l, r):
            if l > r:
                return None
            if l >= len(vals):
                return None
            
            med = getMedian(l,r)
            #print(l, r, med)
            node = TreeNode(vals[med])
            node.left = buildSubtree(l, med-1)
            node.right = buildSubtree(med+1, r)
            
            return node
            
        root = buildSubtree(0, len(vals))
        return root