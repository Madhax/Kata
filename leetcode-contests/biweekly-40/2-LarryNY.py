# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cheat = []
        
        current = list1
        while current is not None:
            cheat.append(current.val)
            current = current.next
            
        cheat2 = []
        current = list2
        while current is not None:
            cheat2.append(current.val)
            current = current.next
            
        cheat3 = cheat[:a] + cheat2 + cheat[b+1:]
        
        if len(cheat3) == 0:
            return None
        
        head = ListNode(cheat3[0])
        current = head
        for x in cheat3[1:]:
            current.next = ListNode(x)
            current = current.next
        return head
