class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
       
        def countHighest(L, lowestIndex=True):
            ctr = [0]*7
            for item in L:
                ctr[item] += 1
           
            #print(ctr)
            maxValue = 0
            maxIndex = 0
            for x in range(1, len(ctr)):
                if lowestIndex and maxValue < ctr[x]:
                    maxValue = ctr[x]
                    maxIndex = x
               
                elif maxValue <= ctr[x]:
                    maxValue = ctr[x]
                    maxIndex = x
                   
            return maxIndex
       
        topVal = countHighest(A)
        botVal = countHighest(B, False)
        #print(topVal, botVal)
        resultA = True
        resultB = True
       
        Actr = 0
        Bctr = 0
        for x in range(0, len(A)):
            if resultA and A[x] != topVal:
                if B[x] != topVal:
                    resultA = False
                else:
                    Actr += 1
                   
            if resultB and B[x] != botVal:
                if A[x] != botVal:
                    resultB = False
                else:
                    Bctr += 1
                   
        if resultA and resultB:
            return min(Actr, Bctr)
        elif resultA:
            return Actr
        elif resultB:
            return Bctr
   
        return -1
