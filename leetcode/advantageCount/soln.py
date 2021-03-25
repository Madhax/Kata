class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
       
        AHeap = []
        BHeap = []
        ignored = []
       
        output = [None] * len(A)
        for (index, val) in enumerate(A):
            heappush(AHeap, (val, index))
       
        for (index, val) in enumerate(B):
            heappush(BHeap, (val, index))
           
           
        while len(BHeap) > 0 and len(AHeap) > 0:
            if AHeap[0][0] <= BHeap[0][0]:
                ignored.append(heappop(AHeap))
                continue
           
            (aval, aindex) = heappop(AHeap)
            (bval, bindex) = heappop(BHeap)
           
            output[bindex] = aval
           
        #push remaining
        for (index, val) in AHeap:
            ignored.append((val, index))
           
        for x in range(0, len(output)):
            if output[x] == None:
                (val, _) = ignored.pop()
                output[x] = val
               
        return output
