class MyCircularQueue:

    def __init__(self, k: int):
        self._data = [None]*k
        self._size = 0
        self._cacipity = k
        self._front = 0
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self._data[(self._front+self._size)%self._cacipity] = value
        self._size+=1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._data[self._front] = None
        self._front = (self._front+1)%self._cacipity
        self._size-=1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self._front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear = (self._front + self._size-1)%self._cacipity
        return self._data[rear]

    def isEmpty(self) -> bool:
        return self._size ==0

    def isFull(self) -> bool:
        return self._size ==self._cacipity