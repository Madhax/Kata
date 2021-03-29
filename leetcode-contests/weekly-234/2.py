class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
        ops = 0
        orig = list(range(n))
        prem = list(range(n))
        
        arr = list(range(n))
        
        while True:
            for x in range(len(prem)):
                if x % 2 == 0:
                    arr[x] = prem[int(x/2)] 
                else:
                    arr[x] = prem[int(n / 2 + (x - 1) / 2)]
                    
            ops += 1
            prem[:] = arr[:]
            if orig == prem:
                break
            
        return ops