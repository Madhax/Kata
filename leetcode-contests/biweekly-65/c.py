class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()
        maxArray = []
        maxBeauty = 0
        for price, beauty in items:
            maxBeauty = max(beauty, maxBeauty)
            maxArray.append((price, maxBeauty))
            
        #print(maxArray)
        output = []
        
        for q in queries:
            idx = bisect.bisect_left(maxArray, (q, math.inf))
            if 0 < idx <= len(maxArray):
                output.append(maxArray[idx-1][1])
            else:
                output.append(0)
            
        return output
