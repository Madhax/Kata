class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        
        work = []
        best = -math.inf
        for val in points:
            #print(val, work)
            while work and val[0]-work[0][1] > k:
                heappop(work)
            
            if work:
                best = max(best, -work[0][0] + val[0] + val[1])
                
            heappush(work, (val[0]-val[1], val[0]))
            
        return best
            
            