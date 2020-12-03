# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    d = {}
    length = 0
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        index = 0
        node = head
        self.d[index] = node
        while node.next:
            node = node.next
            index += 1
            self.d[index] = node
       
        self.length = index

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.d[random.randint(0, self.length)].val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
