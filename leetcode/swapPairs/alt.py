# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None
        if not head.next: return head
        
        p = head.next
        head.next = self.swapPairs(head.next.next)
        p.next = head
        
        return p
        