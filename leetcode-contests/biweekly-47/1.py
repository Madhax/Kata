class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        def distance(x1, x2, y1, y2):
            return abs(x1-x2) + abs(y1-y2)
        
        bestIndex = -1
        bestDistance = math.inf
        
        for index, point in enumerate(points):
            #print(x, y, point[0], point[1])
            dist = distance(x, point[0], y, point[1]) 
            if point[0] == x or point[1] == y:
                if dist < bestDistance:
                    bestIndex = index
                    bestDistance = dist
                    
        return bestIndex