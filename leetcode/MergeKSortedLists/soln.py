# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #unwind
        if len(lists) == 0:
            return None
        
        vals = []
        for list in lists:
            while list:
                vals.append(list.val)
                list = list.next
                
        vals.sort()
        #print(vals)
        if len(vals) == 0:
            return None
        head = ListNode(vals[0])
        node = head
        for x in range(1, len(vals)):
            node.next = ListNode(vals[x])
            node = node.next
            
        node.next = None
        return head
    