"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    # naive solution.
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        hash_table = dict()
        m = n = head
        
        while m:
            hash_table[m] = Node(m.val)
            m = m.next
        
        while n:
            # if n.next in hash_table:
            #     hash_table[n].next = hash_table[n.next]
            # if n.random in hash_table:
            #     hash_table[n].random = hash_table[n.random]
            
            hash_table[n].next = hash_table.get(n.next)
            hash_table[n].random = hash_table.get(n.random)
            n = n.next
        
        return hash_table[head]