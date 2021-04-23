class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        brickCounter = Counter()
        
        for row in wall:
            index = 0
            for column in row:
                index += column
                brickCounter[index] += 1
            
        minCross = math.inf
        #print(brickCounter, index, len(wall))
        for key in brickCounter.keys():
            if key != index:
                minCross = min(minCross, len(wall) - brickCounter[key])
        
        return minCross if minCross != math.inf else len(wall)