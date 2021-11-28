class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        #it is presum, but need posn of next plate, and prior plate
        nextPlates = []
        priorPlates = []

        lplate = s.find("|")
        rplate = s.rfind("|")
        
        sr = s[::-1]
        if lplate == -1 or (lplate==rplate):
            return [0] * len(queries)
        
        nextPlate = lplate
        for x in range(len(s)):
            if nextPlate == -1:
                nextPlates.append(nextPlate)
            elif x <= nextPlate:
                nextPlates.append(nextPlate)
            else:
                nextPlate = s.find("|", nextPlate+1)
                nextPlates.append(nextPlate)
                
        priorPlate = sr.find("|")
        for x in range(len(sr)):
            if priorPlate == -1:
                priorPlates.append(priorPlate)
            elif x <= priorPlate:
                priorPlates.append(len(sr)-priorPlate-1)
            else:
                priorPlate = sr.find("|", priorPlate+1)
                if priorPlate == -1:
                    priorPlates.append(priorPlate)
                else:
                    priorPlates.append(len(sr)-priorPlate-1)
        
        priorPlates.reverse()
        #print(nextPlates, priorPlates)
        preSum = []
        curPlates = 0
        for idx, c in enumerate(s):
            if c == "*" and lplate <= idx <= rplate:
                curPlates += 1
                preSum.append(curPlates)
                
            else:
                preSum.append(curPlates)
                
                
        output = []
        for q in queries:
            lb = nextPlates[q[0]]
            ub = priorPlates[q[1]]
            
            #print(lb, ub)
            if lb == -1 or ub == -1:
                output.append(0)
            else:
                output.append(max(0, preSum[ub] - preSum[lb]))
            
        return output
