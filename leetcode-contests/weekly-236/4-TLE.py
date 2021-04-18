
import collections
import sortedcontainers
class MKAverage:
    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.que = collections.deque([])
        self.slist = sortedcontainers.SortedList()
        

    def addElement(self, num):
        self.que.append(num)
        self.slist.add(num)
        if len(self.que) > self.m:
            lru = self.que.popleft()
            self.slist.remove(lru)

            
    def calculateMKAverage(self):
        if len(self.que) < self.m:
            return -1
        return sum(self.slist[self.k:-self.k]) // (self.m - 2*self.k)
        