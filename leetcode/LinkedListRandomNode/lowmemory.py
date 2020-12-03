# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randrange
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        counter = 1
        node = self.head
        result = None
        while node:
            rand_val = randrange(counter)
            if rand_val < 1:
                result = node.val
            node = node.next
            counter += 1
        return result