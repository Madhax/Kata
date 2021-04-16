# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lessThan = []
        greaterThan = []
        node = head
        while node:
            if node.val >= x:
                greaterThan.append(node.val)
            else:
                lessThan.append(node.val)
            node = node.next
                
        if len(lessThan) > 0:
            newhead = ListNode(lessThan[0])
            curnode = newhead
            for x in range(1, len(lessThan)):
                newnode = ListNode(lessThan[x])
                curnode.next = newnode
                curnode = newnode
            for x in range(0, len(greaterThan)):
                newnode = ListNode(greaterThan[x])
                curnode.next = newnode
                curnode = newnode
            return newhead
        elif len(greaterThan) > 0:
            newhead = ListNode(greaterThan[0])
            curnode = newhead
            for x in range(1, len(greaterThan)):
                newnode = ListNode(greaterThan[x])
                curnode.next = newnode
                curnode = newnode
            return newhead
        else:
            return None
        
        