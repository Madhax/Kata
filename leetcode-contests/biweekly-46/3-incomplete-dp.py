class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])
        seen = set()
        hasWater = set()
        
        @functools.cache
        def getMinimumDistance(y, x, step):
            nonlocal hasWater, seen
    
            if y >= R or y < 0 or x >= C or x < 0:
                return math.inf
            
            if (y,x) in seen:
                return math.inf
        
            if (y,x) in hasWater:
                return 0
            
            steps = math.inf
            
            seen.add((y, x))
            steps = min(steps, 1 + getMinimumDistance(y-1, x, step+1) )
            
            steps = min(steps, 1 + getMinimumDistance(y+1, x, step+1) )
            
            steps = min(steps, 1 + getMinimumDistance(y, x+1, step+1) )
            
            steps = min(steps, 1 + getMinimumDistance(y, x-1, step+1) )
            
            seen.remove((y,x))
            
            return steps
        
        for y, row in enumerate(isWater):
            #print(row)
            for x, val in enumerate(row):
                #print(val)
                if val == 1:
                    hasWater.add((y,x))
                    
        #print(hasWater)
        #print(getMinimumDistance(0,0))
        
        output = []
        
        for y in range(R):
            output.append([])
            for x in range(C):
                #print(y,x)
                output[y].append(getMinimumDistance(y,x, 0))
        
        return output
            
        