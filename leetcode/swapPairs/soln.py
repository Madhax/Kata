# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #constraint - only swap
       
        def fetch(node, k):
            s = deque()
            while node and k:
                #print(node.val)
                s.append(node)
                node = node.next
                k -= 1
               
            return (s, node)
       
        #
        node = head
        head = ListNode(0)
        startNode = head
        while True:
            work = fetch(node, 2)
            if len(work[0]) == 0:
                break
               
            while len(work[0]) > 0:
                startNode.next = work[0].pop()
                startNode = startNode.next
                #print(startNode.val)
               
            node = work[1]
       
        startNode.next = None
       
        return head.next
       
       
        #print(fetch(head, 2))