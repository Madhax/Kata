class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:

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

            degrees = math.atan2(y,x)                
            coordinates.append(degrees)
            #print(coordinates)
        
        coordinates.sort()
        #print(coordinates)
        coordinates = coordinates + [x + 2.0 * math.pi for x in coordinates]
        angle = math.pi * angle / 180
        
        #print(coordinates)

        lptr = 0
        rptr = 0
        best = 0
        for rptr in range(len(coordinates)):
            while coordinates[rptr] - coordinates[lptr] > angle:
                lptr += 1
                
            best = max(best, rptr-lptr+1)
                
        return best + alwaysVisible
        """
        while True:
            curMax = coordinates[rptr]
            monoq.append(curMax)
            while angleDiff(curMax, curMin) > angle:
                
            rptr += 1  
            if rptr == len(coordinates):
                rptr = 0
            
            if len(monoq)+alwaysVisible > best:
                #print("here", monoq)
                best = len(monoq) + alwaysVisible

            if rptr == lptr:
                return best
        """
        
            
            #print(monoq, lptr, rptr)
            
            
            
            
            
        return 0
        