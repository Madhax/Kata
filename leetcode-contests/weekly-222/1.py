class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        size = 0
        boxIter = 0
        while truckSize > 0:
            try:
                if boxTypes[boxIter][0] > 0:
                    boxTypes[boxIter][0] -= 1
                    size += boxTypes[boxIter][1]
                    truckSize -= 1

                else:
                    boxIter += 1
            except:
                break
        return size