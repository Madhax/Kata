# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        if headA == None or headB == None:
            return None
       
        d[id(headA)] = headA
       
        while headA.next:
            headA = headA.next
            d[id(headA)] = headA
           
        if id(headB) in d:
            return headB

        while headB.next:
            headB = headB.next
            if id(headB) in d:
                return headB
       
        return None