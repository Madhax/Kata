from heapq import *
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        
        h = []
        
        heappush(h, -a)
        heappush(h, -b)
        heappush(h, -c)
        score = 0
        while True:
                val1 = heappop(h)
                val2 = heappop(h)
                
                if val1 >= 0 or val2 >= 0:
                    break
                    
                score += 1
                
                heappush(h, val1+1)
                heappush(h, val2+1)
                    
        return score