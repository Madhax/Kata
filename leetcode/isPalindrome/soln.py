# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        output = []
        
        node = head
        while node:
            output.append(node.val)
            node = node.next
        
        return output == output[::-1]