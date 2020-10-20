from functools import *
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        
        def distance(x,y,towerx, towery):
            return float(sqrt((x-towerx)**2 + (y-towery)**2))
        
        def isReachable(x, y, towerx, towery, radius):
            return distance(x,y,towerx,towery) <= radius
        
        def signalQuality(x, y, towerx, towery, quality):
            return floor(float(quality)/(1+distance(x,y,towerx,towery)))
        
        minx = 51
        maxx = 0
        miny = 51
        maxy = 0
        
        for tower in towers:
            if tower[0] < minx:
                minx = tower[0]
            if tower[0] > maxx:
                maxx = tower[0]
            if tower[1] < miny:
                miny = tower[1]
            if tower[1] > maxy:
                maxy = tower[1]
            
        
        bestLocation = None
        MaxQuality = 0
        
        for x in range(0, 51):
            for y in range(0, 51):    
                currentQuality = 0
                for tower in towers:
                    if isReachable(x,y, tower[0], tower[1], radius):
                        currentQuality += signalQuality(x,y, tower[0], tower[1], tower[2])
                        #if (x == 45 or x == 42) and (y == 36 or y == 44):
                        #    print(x,y,currentQuality)
                
                if currentQuality > MaxQuality:
                    MaxQuality = currentQuality
                    bestLocation = [x,y]
                    
        return bestLocation
        