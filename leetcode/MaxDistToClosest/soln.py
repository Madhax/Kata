class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
       
        bestDiff = 0
        iter = 0    
        startRange = -1
        while iter < len(seats):
            #print(bestDiff, iter, startRange)
            if seats[iter] == 0:
                if startRange == -1:
                    startRange = iter
                iter += 1
                continue
               
            else:
                if startRange > 0:
                    diff = ceil((iter - startRange)/2)
                    if diff > bestDiff:
                        bestDiff = diff
                    startRange = -1
                if startRange == 0:
                    diff = (iter - startRange)
                    if diff > bestDiff:
                        bestDiff = diff
                    startRange = -1
                iter += 1
       
        if startRange >= 0:
            diff = iter-startRange
            if diff > bestDiff:
                bestDiff = diff
               
        return bestDiff
