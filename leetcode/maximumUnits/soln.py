class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        
        units = 0
        iter = 0
        while truckSize > 0 and iter < len(boxTypes):
            diff = min(truckSize, boxTypes[iter][0])
            units += (boxTypes[iter][1] * diff)
            boxTypes[iter][0] -= diff
            if boxTypes[iter][0] == 0:
                iter += 1
                
            truckSize -= diff
        return units