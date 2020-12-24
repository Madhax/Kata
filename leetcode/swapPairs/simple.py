# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        self.swapPairsHelper(head)
        return head
    
    def swapPairsHelper(self, curHead) -> None:
        if not curHead or not curHead.next:
            return
        curHead.val, curHead.next.val = curHead.next.val, curHead.val
        self.swapPairsHelper(curHead.next.next)