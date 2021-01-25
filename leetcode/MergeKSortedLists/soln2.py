# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
       
        vals = []
        for ll in lists:
            while ll:
                vals.append(ll.val)
                ll = ll.next
       
       
        vals.sort()
        print(vals)
        head = ListNode(0)
        node = head
        for val in vals:
            node.next = ListNode(val)
            node = node.next
           
        return head.next