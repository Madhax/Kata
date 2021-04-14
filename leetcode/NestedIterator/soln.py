# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        s = []
        self.output = []
        self.index = 0
        current = nestedList
        iterator = 0
        while True:
            #print(iterator)
            if iterator == len(current):
                if len(s) > 0:
                    (current, iterator) = s.pop()
                    continue
                else:
                    break
            if current[iterator].isInteger():
                self.output.append(current[iterator].getInteger())
            else:
                newList = current[iterator].getList()                
                s.append((current, iterator+1))
                current = newList
                iterator = 0
                continue
            iterator += 1
        #print(self.output)
               
    def next(self) -> int:
        self.index+=1
        return self.output[self.index-1]
   
   
    def hasNext(self) -> bool:
        return self.index < len(self.output)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())