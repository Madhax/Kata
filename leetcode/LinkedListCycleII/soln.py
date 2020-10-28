# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        d = {}
        node = head
        while node is not None:
            if id(node) in d:
                return d[id(node)]
            else:
                d[id(node)] = node
               
            node = node.next
           
        return None