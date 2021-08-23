class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def getArea(width):
            prev, area = 0, 0
            for bottom, top in intervals:
                bottom = max(bottom, prev)
                if top > bottom:
                    area += (top - bottom) * width
                    prev = top
            return area
                
        MOD = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2)) # 1: start; 2: end
            events.append((x2, 1, y1, y2))   
        events.sort()
        
        area, prevX = 0, 0
        intervals = []
        for curX, type, y1, y2 in events:
            area += getArea(curX - prevX)
            if type == 1:
                intervals.remove((y1, y2))
            else:
                intervals.append((y1,y2))
                intervals.sort()  # sort because new tuple is added
            prevX = curX 
        return area % MOD