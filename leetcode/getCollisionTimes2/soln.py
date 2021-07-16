class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        
        collisions = []        
        s = []

        def calcCollision(p1, s1, p2, s2):
            if s2 == s1:
                return math.inf
            
            return (p1-p2)/(s2-s1)
        
        
        for posn, speed in reversed(cars):
            
            while s and (s[-1][1] > speed or calcCollision(posn, speed, s[-1][0], s[-1][1]) > s[-1][2]):
                s.pop()
                
            if len(s) == 0:
                collisions.append(-1)
                s.append((posn, speed, math.inf))
                continue
                         
            else:
                collTime = calcCollision(posn, speed, s[-1][0], s[-1][1])
                collisions.append(collTime if collTime != math.inf else -1)
                s.append((posn, speed, collTime))
                
            
            
            
        return reversed(collisions)