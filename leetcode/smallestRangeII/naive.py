class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
       
        A.sort()
        backup = A.copy()
        print(A)
       
        currentBest = float("inf")
        for x in range(0, 4):
            A = backup.copy()
            if x == 0:
                A[0] += K
                A[-1] += K
            if x == 1:
                A[0] -= K
                A[-1] -= K
            if x == 2:
                A[0] += K
                A[-1] -= K
               
            if x == 3:
                A[0] -= K
                A[-1] += K
               
            currentMax = max(A[-1], A[0])
            currentMin = min(A[-1], A[0])
            iter = 1
            while iter < len(A)-1:
                if currentMin <= A[iter]+K <= currentMax:
                    A[iter] = A[iter] + K
                elif currentMin <= A[iter]-K <= currentMax:
                    A[iter] = A[iter] - K
                elif A[iter]+K > currentMax:
                    if A[iter]-K < currentMin:
                        ##if x == 2:
                        #    print(currentMax, currentMin, A[iter]+K - currentMax , currentMin-(A[iter]-K))
                        if A[iter]+K - currentMax < currentMin-(A[iter]-K):
                            currentMax = A[iter] + K        
                            A[iter] = A[iter]+K  
                       
                        else:
                            currentMin = A[iter] -K
                            A[iter] = A[iter]-K
                    else:
                        A[iter] = A[iter]-K
                else:
                    print("here")
                    A[iter] = A[iter] + K
                   
   
                iter += 1
            if currentBest > (currentMax-currentMin):
                currentBest = currentMax-currentMin
            print(A)
        return currentBest