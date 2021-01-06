# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = defaultdict(int)
        if head is None:
            return head
        
        node = head
        while node.next:
            d[node.val] += 1
            node = node.next
            
        d[node.val] += 1
        
        newhead = ListNode(0)
        node = newhead
        for key in d.keys():
            if d[key] > 1:
                continue
            else:
                newnode = ListNode(key)
                node.next = newnode
                node = newnode
                
        return newhead.next