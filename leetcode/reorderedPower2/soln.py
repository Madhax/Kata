class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
       
        counterList = []
       
        for x in range(0, 64):
            ctr = Counter(list(str(2**x)))
            #print(2**x)
            counterList.append(ctr)
           
        test = Counter(list(str(N)))
       
        return any(test == x for x in counterList)
