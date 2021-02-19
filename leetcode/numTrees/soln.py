class Solution:
    def numTrees(self, n: int) -> int:
        
        @functools.cache
        def helper(n):
            if n <= 1:
                return 1
            
            output = 0
            for x in range(0,n):
                output += helper(x) * helper(n-x-1)
                
            return output
        
        return helper(n)