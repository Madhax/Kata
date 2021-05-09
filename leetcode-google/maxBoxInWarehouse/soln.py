class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        minHeights = [0] * len(warehouse)
        minHeights[0] = warehouse[0]
        for x in range(1, len(warehouse)):
            minHeights[x] = min(warehouse[x], minHeights[x-1])
            
        numBox = 0
        warehouseIter = len(warehouse) - 1
        while len(boxes) > 0 and warehouseIter >= 0:
            if warehouse[warehouseIter] < boxes[-1] or boxes[-1] > minHeights[warehouseIter]:
                warehouseIter -= 1
                continue
            
            box = boxes.pop()
            warehouseIter -= 1
            numBox += 1
            
        return numBox
            