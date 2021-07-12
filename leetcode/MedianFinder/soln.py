import sortedcontainers

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sl = sortedcontainers.SortedList()

    def addNum(self, num: int) -> None:
        
        self.sl.add(num)

    def findMedian(self) -> float:
        if len(self.sl) == 1:
            return self.sl[0]
        
        if len(self.sl) & 1:
            return self.sl[(len(self.sl)//2)]
        
        else:
            return (self.sl[(len(self.sl)//2)] + self.sl[(len(self.sl)//2)-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()