class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
        sortedList = []
        for idx, color in enumerate(colors):
            sortedList.append((color, idx))
            
        sortedList.sort()
        
        result = []
        
        for idx, color in queries:
            
            posn = bisect.bisect(sortedList, (color, idx))
            
            if posn == 0:
                if sortedList[posn][0] != color:
                    result.append(-1)
                    continue
                    
                result.append(abs(sortedList[posn][1] - idx))
                
            elif posn == len(sortedList):
                if sortedList[posn-1][0] != color:
                    result.append(-1)
                    continue
                    
                result.append(abs(sortedList[posn-1][1] - idx))
                
            else:
                if sortedList[posn-1][0] != color and sortedList[posn][0] != color:
                    result.append(-1)
                    continue
                cand = math.inf
                
                if sortedList[posn-1][0] == color:
                    cand = min(cand, abs(sortedList[posn-1][1] - idx))
                if sortedList[posn][0] == color:
                    cand = min(cand, abs(sortedList[posn][1] - idx))
                result.append(cand)
                    
        return result