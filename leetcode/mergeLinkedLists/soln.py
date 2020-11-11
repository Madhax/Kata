# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
       
        if l1 and l2:
            if l1.val > l2.val:
                node = l2
                l2 = l2.next
            else:
                node = l1
                l1 = l1.next
        elif l1:
            return l1
        elif l2:
            return l2
        else:
            return None
       
        start = node
           
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                    node = node.next
                    continue
                else:
                    node.next = l2
                    l2 = l2.next
                    node = node.next
                    continue
                   
            if l1:
                node.next = l1
                l1 = l1.next
                node = node.next
                continue
           
            if l2:
                node.next = l2
                l2 = l2.next
                node = node.next
                continue
               
               
        return start