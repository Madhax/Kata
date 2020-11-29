class FrontMiddleBackQueue:

    def __init__(self):
        self.left = collections.deque()
        self.right = collections.deque()

    def fix(self):
        if len(self.left) > len(self.right):
            x = self.left.pop()
            self.right.appendleft(x)
            
        while len(self.right) > len(self.left) + 1:
            x = self.right.popleft()
            self.left.append(x)
        
    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        
        self.fix()

    def pushMiddle(self, val: int) -> None:
        self.fix()
        self.left.append(val)
        self.fix()
        

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.fix()

    def popFront(self) -> int:
        if len(self.left) + len(self.right) == 0:
            return -1

        if len(self.left) == 0:
            x = self.right.pop()
            return x
        
        self.fix()
        x = self.left[0]
        self.left.popleft()
        self.fix()
        return x
        
        
    def popMiddle(self) -> int:
        if len(self.left) + len(self.right) == 0:
            return -1

        #print(self.left, self.right)
        self.fix()
        
        if len(self.left) == len(self.right):
            x = self.left.pop()
        else:
            x = self.right.popleft()

        self.fix()
            
        return x

    def popBack(self) -> int:
        if len(self.left) + len(self.right) == 0:
            return -1

        self.fix()
        x = self.right.pop()
        self.fix()
        return x