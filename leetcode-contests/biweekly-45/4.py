from bisect import *

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        #get max non-overlapping values
        
        #sort by start day
        events.sort(key=lambda x: x[0])
        startDays, end, val = zip(*events)
        
        """x
        data = [(3, 1), (2, 2), (5, 6)]
fst, snd = zip(*data)
idx = bisect(fst, 2)
        """
        @functools.cache
        def getMaxValue(day, left):
            
            if left == 0:
                return 0
            
            if day > events[-1][0]:
                return 0
 
            idx = bisect(startDays, day)
            
            bestVal = 0
            for cand in range(idx, len(events)):
                bestVal = max(bestVal,  events[cand][2] + getMaxValue(events[cand][1], left-1))
                
            return bestVal
            
        
        return getMaxValue(0, k)