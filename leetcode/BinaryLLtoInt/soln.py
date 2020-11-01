# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        startVal = 0
        while head:
            
            startVal += head.val
            startVal = startVal << 1
            
            #print(head.val, startVal)
            head = head.next
            
        startVal = startVal >> 1
        return startVal