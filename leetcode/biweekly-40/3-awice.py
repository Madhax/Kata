class FrontMiddleBackQueue:

    def __init__(self):
        self.first = collections.deque()
        self.last = collections.deque()

    def pushFront(self, val: int) -> None:
        self.first.appendleft(val)
        self._rebalance()
        

    def pushMiddle(self, val: int) -> None:
        # print("!", self.first, self.last)
        if len(self.first) == len(self.last):
            self.last.appendleft(val)
        else:
            self.first.append(val)

    def pushBack(self, val: int) -> None:
        self.last.append(val)
        self._rebalance()
        

    def popFront(self) -> int:
        # print("!", self.first, self.last)
        if self.first:
            ans = self.first.popleft()
        elif self.last:
            ans = self.last.popleft()
        else:
            return -1
        self._rebalance()
        return ans

    def popMiddle(self) -> int:
        if len(self.first) == len(self.last):
            if self.first:
                ans = self.first.pop()#appendleft(val)
            else:
                return -1
        elif self.last:
            ans = self.last.popleft()
        else:
            ans = -1
        return ans

    def popBack(self) -> int:
        if self.last:
            ans = self.last.pop()
        elif self.first:
            ans = self.first.pop()
        else:
            return -1
        self._rebalance()
        return ans
    
    def _rebalance(self):
        while len(self.first) > len(self.last):
            self.last.appendleft(self.first.pop())
        while len(self.last) -1 > len(self.first):
            self.first.append(self.last.popleft())

