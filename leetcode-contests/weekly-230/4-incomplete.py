class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        
        alreadyCollided = set()
        
        collisionTimes = []
        output = [-1] * len(cars)
       
        cars = [x for x in enumerate(cars)]
        print(cars)
        while True:
            nextCollision = math.inf
            nextCollisionTime = math.inf
            
            for carIter in range(len(cars)-1):
                if cars[carIter][0] in alreadyCollided:
                    continue
                elif (cars[carIter+1][1][1] - cars[carIter][1][1]) == 0:
                    #collisionTimes.append(math.inf)
                    continue
            
                else:
                    #collisionTimes.append( (cars[carIter][0] - cars[carIter+1][0]) / (cars[carIter+1][1] - cars[carIter][1]))
                    timeToCollide = (cars[carIter][1][0] - cars[carIter+1][1][0]) / (cars[carIter+1][1][1] - cars[carIter][1][1])
                #print(timeToCollide)
                if timeToCollide >= 0 and timeToCollide < nextCollisionTime:
                    nextCollision = cars[carIter][0] 
                    nextCollisionTime = timeToCollide
            
            if nextCollision == math.inf:
                break
            else:
                #print(nextCollision)
                alreadyCollided.add(nextCollision)
                
            
                
        print(collisionTimes)
        
        return output
            
            