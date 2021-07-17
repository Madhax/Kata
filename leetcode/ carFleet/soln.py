class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0
        data = [(posn, carSpeed) for posn, carSpeed in zip(position, speed)]
        data.sort()
        collisions = []
        #print(data)
        for posn, carSpeed in data:
            
            #target = posn + speed*time
            TimeToTarget = (target - posn) / carSpeed
            collisions.append(TimeToTarget)
            
            
        #print(collisions)
        """
        lessThans = 0
        for x in range(len(collisions)-1):
            if collisions[x] <= collisions[x+1]:
                lessThans += 1
                collisions[x+1] = collisions[x]
                
        """
        maxTime = collisions[-1]
        for x in range(len(collisions)-2, -1, -1):
            maxTime = max(collisions[x], maxTime)
            collisions[x] = maxTime
            
        return len(set(collisions))
            
        