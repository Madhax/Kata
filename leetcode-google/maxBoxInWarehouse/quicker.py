class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        # ans = 0
        # boxes.sort(reverse=True)
        # print (boxes)
        # bi, wi = 0, 0
        # while bi<len(boxes) and wi<len(warehouse):
        #     if boxes[bi]<=warehouse[wi]:
        #         ans+=1
        #         bi+=1
        #         wi+=1
        #     else:
        #         bi+=1
        # return ans
        
        blen, wlen = len(boxes), len(warehouse)
        
        used = 0
        
        for box in sorted(boxes, reverse=True):
            if used <wlen and box<=warehouse[used]:
                used+=1
                if used==blen:
                    return used
        return used