from collections import deque

class FrontMiddleBackQueue:
    c = None
    def __init__(self):
        self.c = []

    def pushFront(self, val: int) -> None:
        self.c.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        dlen = len(self.c)
        mid = dlen/2
        if dlen%2 != 0:
            mid = floor(mid)
        else:
            mid = int(mid)
            
        print(val, dlen, mid)
        self.c.insert(mid, val)
        

    def pushBack(self, val: int) -> None:
        self.c.append(val)

    def popFront(self) -> int:
        if len(self.c) > 0:
            return self.c.pop(0)
        else:
            return -1
        

    def popMiddle(self) -> int:
        dlen = len(self.c)
        mid = dlen/2
        if dlen%2 == 0:
            mid = floor(mid) - 1
            
        else:
            mid = int(mid)
            
        print(dlen, mid, self.c)
            
        if dlen > 0:
            return self.c.pop(mid)
        else:
            return -1

    def popBack(self) -> int:
        if len(self.c) > 0:
            return self.c.pop()
        else:
            return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()