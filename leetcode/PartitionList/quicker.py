# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        e1, e2 = dummy1, dummy2
        while head:
            if head.val < x:
                e1.next = head
                e1 = e1.next
            else:
                e2.next = head
                e2 = e2.next
            head = head.next

        e2.next = None  #e2 will be atleast dummy, hence no need to check whether e2 exists or not
        e1.next = dummy2.next
    
        return dummy1.next