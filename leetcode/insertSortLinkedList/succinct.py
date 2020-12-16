# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        tail = head
        
        while tail.next:
            insert_node = tail.next
            
            if tail.val <= insert_node.val:
                tail = tail.next
            else:
                tail.next = insert_node.next

                temp = dummy
                while temp.next.val < insert_node.val:
                    temp = temp.next
            
                insert_node.next = temp.next
                temp.next = insert_node
            
                # tail = tail.next
        return dummy.next