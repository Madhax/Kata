from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        
        posn = bisect.bisect(self.events, (start, 1))
        #print(self.events, posn, len(self.events))
    
        if len(self.events) > 0:
            
            if posn == 0 and self.events[0][0] < end:
                #print("h1")
                return False
                
            elif posn == len(self.events) and self.events[posn-1][0] > start:
                #print("h2")
                return False
                
            elif self.events[posn-1][1] == 1:
                #print("h3")
                return False
            
            elif posn < len(self.events) and (self.events[posn][1] == 0 or self.events[posn][0] < end):
                #print("h4")
                return False
            
            
            #previous is end and less than start
            
            #next is start and greater than end
        self.events.add((start, 1))
        self.events.add((end, 0))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)