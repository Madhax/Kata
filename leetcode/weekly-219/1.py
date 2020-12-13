class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        def countMatches(n):
            #print(n)
            if n == 2:
                return 1
        
            if n < 2:
                return 0
            
            if n % 2 == 0:
                return (n/2) + countMatches(n/2)
            
            else:
                return (n-1)/2 + countMatches((n-1)/2 + 1)
    
        return int(countMatches(n))