# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        tail = head
        while tail:
            if tail.next in visited:
                return tail.next
            visited.add(tail)
            tail = tail.next
        return None