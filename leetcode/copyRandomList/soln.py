"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #return copy.deepcopy(head)
        nodeiter = head
        oldnode = {}
        newnode = {}
       
        oldnodeiter = head
        newnodeiter = Node(0)
        newnodehead = newnodeiter
        while oldnodeiter:
            curId = id(oldnodeiter)
            if curId not in oldnode:
                oldnode[curId] = oldnodeiter
                newnode[curId] = copy.copy(oldnode[curId])

            newnodeiter.next = newnode[curId]
            newnodeiter = newnodeiter.next
            #newnodeiter.next = None
            #newnodeiter.random = None
            if oldnodeiter.random is not None:
                randomId = id(oldnodeiter.random)
                if randomId not in oldnode:
                    oldnode[randomId] = oldnodeiter.random
                    newnode[randomId] = copy.copy(oldnode[randomId])
               
                newnodeiter.random = newnode[randomId]
               
            oldnodeiter = oldnodeiter.next
       
        """
        iter = newnodehead.next
        while iter:
            print(iter.val, iter.random.val if iter.random else None)
            iter = iter.next
           
        test = Node(0)
        test.random = Node(1)
        test.next = test.random
        #return test
        #print(newnodehead.next.val, newnodehead.next.next.val)"""
        return newnodehead.next