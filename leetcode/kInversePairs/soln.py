class Solution:

    def kInversePairs(self, n: int, k: int) -> int:
        m =  n*(n-1)//2
        
        k = min(m-k, k) 
        
        if k < 0:
            return 0
        if k == 0:
            return 1
        if k == 1:
            return n-1
       
        arr = [0]*(k+1)
        arr[0] = 1
        
        for i in range(2, n+1):
            sofar = 0
            windowLeft = 0
            newArr = []
            for j in range(0, k+1):
                if j+1-windowLeft > i:
                    # window full
                    sofar -= arr[windowLeft]
                    windowLeft += 1
                sofar += arr[j]
                newArr.append(sofar)
            arr = newArr
        return arr[-1]%1000000007