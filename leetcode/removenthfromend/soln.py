# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = {}
        x = 0
        while head:
            d[x] = head
            head = head.next
            x += 1
            
        d[x] = head
        if x - n == 0:
            head = d[1]
            return head
        else:
            d[x-n-1].next = d[x-n+1]
            return d[0]
        