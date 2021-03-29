class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        #is X the max value at i
        #sum 0 to i, + i -> n < maxSum
        
        def maxSum2(val, index, n):
            
            diff = val - (index+1)
            
            prefix = val*(val+1)//2
            if diff > 0:
                prefix -= diff*(diff+1)//2
            elif diff < 0:
                prefix += (diff) * -1
                
            
            suffix = val*(val+1)//2-val
            diff = (index+val)
            #print(diff)
            if diff >= n:
                suffix -=  (diff-n)*(diff-n+1)//2
                
            elif diff < n:
                suffix += (n-diff)
            
            return prefix+suffix
            
            
        #binary search maxSum
        
        #print(maxSum(7, 1, 4))
        print(maxSum2(2, index, n))
        
        left, right = 0, 10**11 # could be [0, n], [1, n] etc. Depends on problem
        while left < right:
            mid = left + (right - left) // 2
            if maxSum2(mid, index, n) > maxSum:
                #print(maxSum2(mid, index, n), maxSum)
                right = mid
            else:
                #print(maxSum2(mid, index, n), maxSum)
                left = mid + 1
                
        return left-1