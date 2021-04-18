# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = {}
        iter = 0
        node = head
        while node:
            d[iter] = node
            node = node.next
            iter += 1
            
        if n == iter:
            if 1 in d:
                return d[1]
            else:
                return None
        
        offset = iter - n
        if offset+1 in d:
            d[offset-1].next = d[offset+1]
        else:
            d[offset-1].next = None
        return head
