class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        #y = mx + b
        
        #300 * 300 pts comparison
        
        def doesIntersect(slope, intercept, y, x):
            #print(slope, intercept, y, x, (slope * x) + intercept)
            return abs(y -((slope * x) + intercept)) < 0.0001
        
        
        def getEquation(x1, y1, x2, y2):
            if x2 == x1:
                return (math.inf, math.inf)
            
            slope = (y2-y1)/(x2-x1)
            intercept = y1 - (slope*x1)    
            return (slope, intercept)
        
        
            
        counted = set()
        best = 1
        for x in range(len(points)):
            for y in range(x+1, len(points)):
                
                x2, y2 = points[x]
                x1, y1 = points[y]
                
                (slope, intercept) = getEquation(x1, y1, x2, y2)
                
                if (slope, intercept) in counted:
                    continue
                    
                counted.add((slope,intercept))
                #print(slope, intercept)
                ctr = 2
                for z in range(len(points)):
                    if z == y or z == x:
                        continue
                        
                    if slope == 0 and points[z][1] == points[y][1]:
                        ctr += 1
                        continue
                    
                    if slope==math.inf and points[z][0] == points[y][0]:
                        ctr += 1
                        continue
                        
                    if doesIntersect(slope, intercept, points[z][1], points[z][0]):
                        ctr += 1
                if ctr == 10:
                    print(slope, intercept)
                best = max(best, ctr)
                
        
        return best
        
        