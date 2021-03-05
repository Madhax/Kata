# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB  = headB
        while currA:
            while(currB):
                if currA==currB:
                    return currA
                else:
                    currB = currB.next
            currB=headB
            currA = currA.next
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        currA = headA
        currB  = headB
        hashT = {}
        while currA:
            hashT[currA] = currB
            currA = currA.next
        while currB:
            if currB in hashT:
                return currB
            currB = currB.next 