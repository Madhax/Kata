# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        node = head
        nodelist = []
        while node.next:
            nodelist.append(node.val)
            node  = node.next
            
        nodelist.append(node.val)
        
        tmp = nodelist[k-1]
        nodelist[k-1] = nodelist[-k]
        nodelist[-k] = tmp
        
        newhead = ListNode(0)
        node = newhead
        for item in nodelist:
            newnode = ListNode(item)
            node.next = newnode
            node = node.next
        
        return newhead.next
            
            