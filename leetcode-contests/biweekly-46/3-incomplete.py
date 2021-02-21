class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])
        seen = set()
        hasWater = set()
        
        output = []
        
        for y in range(R):
            output.append([])
            for x in range(C):
                #print(y,x)
                output[y].append(math.inf)
                
        
        
        for water in hasWater:
            output[water[0]][water[1]] = 0
            
        hasChanged = True
        
        while hasChanged:
            hasChanged = False
            
            y = 0
            while y < R:
                x = 0
                while x < C:
                    if output[y][x] == math.inf:
                        
                        if y > 0:
                            if output[y-1][x] != math.inf:
                                output[y][x] = min(output[y][x], output[y-1][x]+1)
                                hasChanged =  True
                            if output[y]
        
        
        
        return output
            
        