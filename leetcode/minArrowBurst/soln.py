class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def calculateHits(x, points, startingPoint):
            iter = startingPoint
            hit = 0
            while points[iter][0] <= x:
                if points[iter][0] <= x <= points[iter][1]:
                    hit += 1
                else:
                    return hit
                iter += 1
                if iter == len(points):
                    return hit
        
            return hit

        points.sort()

        if len(points) == 0:
            return 0

        #print(points)
        
        totalHit = 0
        startX = 0
        offset = 0
        while startX != len(points):
            bestHit = 0
            bestX = None
            x = points[startX][0]
            iter = startX
            while x < points[startX][1]+1:
                hits = calculateHits(x, points, startX)
                #print(x, hits,startX)
                if hits > bestHit:
                    bestHit = hits
                    bestX = x
                iter += 1
                if iter == len(points):
                    break
                x = points[iter][0]
                
            startX += bestHit
            totalHit += 1
            
        return totalHit