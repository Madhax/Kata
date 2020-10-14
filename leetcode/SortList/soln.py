# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
           
            if l1.val < l2.val:
                node = l1
                l1 = l1.next
            else:
                node = l2
                l2 = l2.next
               
            head = node
            while l1 and l2:
                if l1.val <= l2.val:
                    node.next = l1
                    node = l1
                    l1 = l1.next
 
                elif l2.val <= l1.val:
                    node.next = l2
                    node = l2
                    l2 = l2.next

            while l1:
                node.next = l1
                node = l1
                l1 = l1.next

            while l2:
                node.next = l2
                node = l2
                l2 = l2.next
                   
            return head
       
        def mergeSort(head, length):
            iter = 1
            if length == 1:
                return head
            pivot = head
            pivotLength = length/2
            while iter < pivotLength:
                iter += 1
                pivot = pivot.next
                         
            parent = pivot
            pivot = pivot.next
            parent.next = None
           
            l = mergeSort(head, iter)
            r = mergeSort(pivot, length-iter)
            head = merge(l,r)
           
            return head
       
        if head == None:
            return head
       
        length = 1
        node = head
        while node.next is not None:
            node = node.next
            length += 1
           
        head = mergeSort(head, length)
        return head
