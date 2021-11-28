class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
        events = []
        
        for start, end, color in segments:
            events.append((start, color))
            events.append((end, -color))
            
        
        events.sort()
        #print(events)
        
        output = []
        curColor = 0
        prevPosn = None
        while events:
            posn, color = events.pop(0)
            
            if prevPosn != None and curColor > 0:
                output.append([prevPosn, posn, curColor])
                prevPosn = posn
            else:
                prevPosn = posn
                
                
            curColor += color
            while events and posn == events[0][0]:
                _, color = events.pop(0)
                curColor += color
                
            
                
        return output
                
            
