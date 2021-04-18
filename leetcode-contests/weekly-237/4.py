class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        output = []
        if len(arr1) == 1 and len(arr2)==1:
            return arr1[0] & arr2[0]
        
        ret = None
        arr1bits = [0 for _ in range(64)]
        arr2bits = [0 for _ in range(64)]
        
        
        arr1bits0 = [0 for _ in range(64)]
        arr2bits0 = [0 for _ in range(64)]
        for i in range(0, 64):
            for val in arr1:
                if val >= (1 << i):
                    if val & (1 << i):
                        arr1bits[i] += 1
                    else:
                        arr1bits0[i] += 1
                        
            for val in arr2:
                if val >= (1 << i):
                    if val & (1 << i):
                        arr2bits[i] += 1
                    else:
                        arr2bits0[i] += 1

                    
        #print(zeroes, ones)
        
        
        start = arr1[0] & arr2[0]
        
        """
        for i in range(0, 64):
            if start >= (1 << i):
                if start & (1 << i):
                    ones[i] -= 1
                else:
                    zeroes[i] -= 1

        """
        val = 0
        #print(arrbits1, arrbits2)
        for i in range(0, 64):
            bitval = (arr1bits[i] * arr2bits[i]) % 2

                
            #zeroes[i] %= 2
            
            
            val |= (bitval<< i)
            #print(i, ones[i], val)
            
            
        return val
        
        #return val
