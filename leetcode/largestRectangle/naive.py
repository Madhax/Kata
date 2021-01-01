class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #min height across x1->x2
        
        #n*2 is trivial
        
        if len(heights) == 1:
            return heights[0]
        
        maxRectangle = 0
        x1 = 0
        while x1 < len(heights):
            lowestHeight = heights[x1]
            area = (1) * lowestHeight
            if area > maxRectangle:
                    maxRectangle = area
                    
            prevArea = area
            x2 = x1 + 1
            while lowestHeight > 0 and x2 < len(heights):
                if lowestHeight > heights[x2]:
                    lowestHeight = min(lowestHeight, heights[x2])

                area = (x2-x1+1) * lowestHeight
                    
                print(x2, x1, area)
                if area > maxRectangle:
                    maxRectangle = area
                    
                if area < prevArea:
                    x1 = x2-1
                    break
            
                x2 += 1
                
            if x2 == len(heights):
                break
                
            x1 += 1
            
        return maxRectangle
                