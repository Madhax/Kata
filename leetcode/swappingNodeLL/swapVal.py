# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nodes=[head]
        cur=head
        while cur:
            cur=cur.next
            if cur:
                nodes.append(cur)
        n1,n2=nodes[k-1],nodes[-k]
        n1.val,n2.val=n2.val,n1.val
        return head
        