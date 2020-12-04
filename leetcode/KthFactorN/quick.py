class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        cur_factor_count = 0
        
        for i in range(1, 1+(n//2)):
            if (n % i == 0):
                cur_factor_count+=1
            
            if(cur_factor_count == k):
                return i
        
        
        if(cur_factor_count + 1 == k):
            return n
        
        return -1
            