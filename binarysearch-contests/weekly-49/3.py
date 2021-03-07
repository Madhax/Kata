class DllNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def __lt__(self, rhs):
        return self.val < rhs.val

    def isPeak(self):
        if self.left is None and self.right is None:
            return True

        elif self.left is None:
            if self.right.val < self.val:
                return True

        elif self.right is None:
            if self.left.val < self.val:
                return True

        elif self.left.val < self.val > self.right.val:
            return True

        return False


class Solution:
    def solve(self, nums):
        heap = []
        output = []
        prevNode = None
        head = None
        for val in nums:
            newnode = DllNode(val)
            if head is None:
                head = newnode
            
            if prevNode is not None:
                prevNode.right = newnode
                newnode.left = prevNode
                newnode.right = None
            else:
                newnode.left = None

            prevNode = newnode
        

        node = head
        while node:
            if node.isPeak():
                heapq.heappush(heap, node)
            node = node.right
        
        while len(heap):
            smallestPeak = heapq.heappop(heap)

            output.append(smallestPeak.val)

            if smallestPeak.left:
                smallestPeak.left.right = smallestPeak.right
            
            if smallestPeak.right:
                smallestPeak.right.left = smallestPeak.left

            if smallestPeak.left and smallestPeak.left.isPeak():
                heapq.heappush(heap, smallestPeak.left)
                
            elif smallestPeak.right and smallestPeak.right.isPeak():
                heapq.heappush(heap, smallestPeak.right)

        return output
