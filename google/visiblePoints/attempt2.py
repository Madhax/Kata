class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        #epsilon = 0.001
        def normalizeAngle(degrees):
            return min(degrees, 360-degrees)
        
        def angleDiff(d1, d2):
            return min(
                max(d1,d2)-min(d1,d2),
                360-max(d1,d2)+min(d1,d2)
                )
            
        #normalize
        for x in range(len(points)):
            points[x][0] -= location[0]
            points[x][1] -= location[1]
            
        coordinates = []
        #print(points)
        alwaysVisible = 0
            
        for x,y in points:
            
            if x == 0 and y == 0:
                alwaysVisible += 1
                continue
            elif x == 0 and y > 0:
                degrees = 90
            elif x == 0 and y < 0:
                degrees = 270
            else:
                degrees = abs(math.degrees(math.atan(y/x)))
                #rint(x,y,degrees)
                if x == 0 and y > 0:
                    degrees = 90

                if x < 0 and y == 0:
                    degrees = 180

                if x < 0 and y < 0:
                    degrees += 180

                if x > 0 and y < 0:
                    degrees += 270
                    
                if x < 0 and y > 0:
                    degrees += 90
                print(x,y,degrees)
                
            coordinates.append(degrees)
            #print(coordinates)
        
        coordinates.sort()
        print(coordinates)
        monoq = deque()
        lptr = 0
        rptr = 0
        curMin = coordinates[0]
        curMax = coordinates[0]
        best = 0
        while True:
            curMax = coordinates[rptr]
            monoq.append(curMax)
            while angleDiff(curMax, curMin) > angle:
                _ = monoq.popleft()
                #print("here", monoq, lptr)
                curMin = monoq[0]
                lptr += 1
                if lptr == len(coordinates):
                    return best
            rptr += 1  
            if rptr == len(coordinates):
                rptr = 0
            
            if len(monoq)+alwaysVisible > best:
                print("here", monoq)
                best = len(monoq) + alwaysVisible

            if rptr == lptr:
                return best
            
            
            #print(monoq, lptr, rptr)
            
            
            
            
            
        return 0
        