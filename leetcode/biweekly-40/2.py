# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        node = list1
        
        #find last node in list2
        lastnode = list2
        while lastnode.next:
            lastnode = lastnode.next
            
        if a == 0:
            #startnode is list2
            iter = b
            node = list1
            while node.next and biter > 0:
                node = node.next
                biter -= 1
            
            taillist1 = node
            
            lastnode = taillist1
            return list2
        
        else:
            iter = 0
            while iter < (a-1):
                node = node.next
                iter += 1

            headlist1 = node
            print(headlist1.val)
            biter = b - a
            
            while node.next and iter != b:
                node = node.next
                iter += 1
            
            taillist1 = node
            print(taillist1.val)
            headlist1.next = list2
            lastnode.next = taillist1.next
            
            return list1
            
            