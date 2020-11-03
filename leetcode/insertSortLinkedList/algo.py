# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node_list = []
        def insert(node):
            l, r = 0, len(node_list)
            while l < r:
                mid = (l + r) // 2
                if node.val > node_list[mid].val:
                    l = mid + 1
                else:
                    r = mid 
            node_list.insert(l, node)
        
        ptr = head
        while ptr:
            insert(ptr)
            ptr = ptr.next 
        
        ptr = dummy = ListNode(-1)
        for node in node_list:
            ptr.next = node
            ptr = ptr.next
        ptr.next = None
        return dummy.next