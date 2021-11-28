class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        rides = list(map(tuple, rides))
        rides.sort(key=lambda x: x[0])
        
        #print(rides)
        
        @functools.cache
        def dp(index):
            nonlocal rides
            if index >= len(rides):
                return 0
            
            best = -math.inf
            #choose
            score = rides[index][1] - rides[index][0] + rides[index][2]
            newindex = bisect.bisect_left(rides, (rides[index][1], 0, 0))
            best = max(best, score + dp(newindex))
            
            #skip
            best = max(best, dp(index+1))
            
            return best
            
            
        
        return dp(0)
        
        #return 0
