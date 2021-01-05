# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
       
        head = None
        if l1 is None:
            return l2
       
        if l2 is None:
            return l1
       
        if l1:
            head = l1
           
        if l2:
            if l2.val < l1.val:
                head = l2
                l2 = l2.next
            else:
                l1=l1.next
               
        currentNode = head
           
        while l1 or l2:
            if l1:
                if l2 and l2.val < l1.val:
                    currentNode.next = l2
                    currentNode = currentNode.next
                    l2 = l2.next
                else:
                    currentNode.next = l1
                    currentNode = currentNode.next
                    l1 = l1.next
            else:
                currentNode.next = l2
                currentNode = currentNode.next
                l2 = l2.next
           
        return head