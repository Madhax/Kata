class Solution:
    def longestMountain(self, A: List[int]) -> int:
       
        increasing = True
        prev = 0
        ctr = 0
        best = 0
        hasIncreased = False
        for x in range(len(A)):
            #print(x, ctr, best, increasing, prev, hasIncreased)  
            if x == 0:
                prev = A[0]
                ctr = 1
                increasing = True
                continue
               
            if increasing:
                if A[x] > prev:
                    #print("increased")
                    hasIncreased = True
                    ctr += 1
                   
                elif A[x] == prev:
                    increasing = True
                    hasIncreased = False
                    ctr = 1
                   
                elif A[x] < prev:
                    increasing = False
                    ctr += 1
               
                prev = A[x]
                   
            else:
                if A[x] < prev:
                    ctr += 1
               
                elif A[x] == prev:
                    if ctr > best and hasIncreased:
                        #print("here")
                        best = ctr
                       
                    hasIncreased = False
                    increasing = True
                    ctr = 1
                   
                elif A[x] > prev:
                    if ctr > best and hasIncreased:
                        #print("here")
                        best = ctr
                       
                    hasIncreased = True
                   
                    increasing = True
                    ctr = 2
                   
            prev = A[x]
           
        #print(x, ctr, best, increasing, prev, hasIncreased)    
        if ctr > best and increasing == False and hasIncreased:
            return ctr
       
        return best