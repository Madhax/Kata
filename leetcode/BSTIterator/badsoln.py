# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    stack = []
    chirality = [] #
    next = 0 #0 - left, 1, - current, 2 - right
    currentNode = None
    isRight = False
    root = None
    ctr = 0
    maxCnt = 0
   
    def __init__(self, root: TreeNode):
        self.stack = []
        self.currentNode = None
        self.isRight = False
        self.chirality = []
        self.root = root
       
        self.ctr = 0
        self.maxCnt = 0
        self.numNodes(root)
       
    def next(self) -> int:
        #print(self.root)
        if self.currentNode == None:
            self.seedNode(self.root)
           
        retVal = self.currentNode.val
        #print(retVal, self.stack, self.chirality, self.isRight)
        self.ctr += 1
        if self.isRight == False and self.currentNode.right is not None:
            #print("1")
            self.stack.append(self.currentNode)
            self.chirality.append(True)
            self.seedNode(self.currentNode.right, False)
           
        elif self.isRight == False and self.currentNode.right is None:
            #print("2")
            if(len(self.stack)):
                self.currentNode = self.stack.pop()
                self.isRight = self.chirality.pop()
            while self.isRight and len(self.stack):
                self.currentNode = self.stack.pop()
                self.isRight = self.chirality.pop()
           
        elif self.isRight == True:
            #print("3")
            #self.stack.pop()
            #self.chirality.pop()
            self.currentNode = self.stack.pop()
            self.isRight = self.chirality.pop()
           
       
        return retVal

    def hasNext(self) -> bool:
        """print(self.isRight, self.currentNode.right is None, len(self.stack), self.chirality)
       
        hasNext = False
        for chirality, node in zip(self.chirality, self.stack):
            if chirality == True:
                continue
            elif node.right is not None:
                hasNext = True
        """
        #print(self.ctr, self.maxCnt)
        return self.ctr != self.maxCnt
       
    def seedNode(self, node, isRight=False):
        #print(node)
        if node.left == None:
            self.currentNode = node
        else:
            self.stack.append(node)
            self.chirality.append(isRight)
            self.seedNode(node.left)
           
    def numNodes(self, node):
        if node is not None:
            self.maxCnt += 1
        if node.left:
            self.numNodes(node.left)
        if node.right:
            self.numNodes(node.right)
           


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()