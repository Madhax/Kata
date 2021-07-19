# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        vals = []
        node = head
        
        while node:
            vals.append(node.val)
            node = node.next
            
        start = 0
        end = k
        
        while end <= len(vals):
            vals[:] = vals[0:start] + vals[start:end][::-1] + vals[end:]
            start = end
            end += k
            
        node = head
        for val in vals:
            node.val = val
            node = node.next
            
        return head
            