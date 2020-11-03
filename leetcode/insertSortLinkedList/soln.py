# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node = head
        newLL = None
        while node:
            nextNode = node.next
            node.next = None
            if newLL == None:
                #print("seed %d" % node.val)
                newLL = node
                
            else:
                newNode = newLL
                
                added = False
                if newLL.val > node.val:
                    #print("prepend %d before %d" % (node.val, newLL.val))
                    node.next = newLL
                    newLL = node
                else:
                    while newNode.next:
                        if newNode.next and newNode.next.val > node.val:
                            #print("insert %d before %d" % (node.val, newNode.next.val))
                            tmp = newNode.next
                            newNode.next = node
                            node.next = tmp
                            added = True
                            break
                        newNode = newNode.next
                        
                    if added == False:
                        #print("append %d" % (node.val))
                        newNode.next = node
                        
            node = nextNode
        
        return newLL
            
        