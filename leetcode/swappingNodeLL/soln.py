# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        nodeList = []
        
        node = head
        
        while node.next:
            nodeList.append(node)
            node = node.next
            
        nodeList.append(node)
        
        nodeList[k-1], nodeList[-k] = nodeList[-k], nodeList[k-1]
        
        #stich
        
        if k>=2:
            nodeList[k-2].next = nodeList[k-1]
        
        if k <= len(nodeList) - 1:
            nodeList[k-1].next = nodeList[k]
        else:
            nodeList[k-1].next = None
            
        if k <= len(nodeList) - 1:
            nodeList[-(k+1)].next = nodeList[-k]
            
        if k > 1:
            nodeList[-k].next = nodeList[-(k-1)]
        else:
            nodeList[-k].next = None
        
        return nodeList[0]
    
        