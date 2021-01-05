# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Catch cases where one list is None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        # Save the head node to return
        head = l2 if l2.val <= l1.val else l1
        
        while l1 is not None and l2 is not None:
            
            # Compare l1 and l2
            bigger = l1 if l1.val >= l2.val else l2
            smaller = l1 if bigger is l2 else l2
            
            # Find the right spot for the bigger node in the smaller list
            while smaller.next is not None and smaller.next.val <= bigger.val:
                smaller = smaller.next
            
            # Save the rest of the smaller list
            l1 = smaller.next
            
            # Splice in the bigger node here
            smaller.next = bigger
            l2 = smaller.next
        
        return head