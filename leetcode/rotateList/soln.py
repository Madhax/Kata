# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None:
            return head
        
        length = 1
        node = head
        while node.next is not None:
            length += 1
            node = node.next
            
        end = node
        offset = k % length
        
        if offset == 0:
            return head
        
        node = head
        iter = length-offset-1
        while iter > 0:
            node = node.next
            iter = iter - 1
            
        if node == end:
            ret = head.next
            head.next = None
            end.next = head
        else:
            end.next = head
            ret = node.next
            node.next = None
        
        return ret
        