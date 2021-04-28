class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """recursion
        def pow3(val):
            if val <= 0:
                return False
            if val == 1:
                return True
            if val % 3 == 0:
                val /= 3
                return pow3(val)
            
            return False
        
        return pow3(n)
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        
        epsilon = (0.00000000001)
        #public boolean isPowerOfThree(int n) {
        #return (Math.log(n) / Math.log(3) + epsilon) % 1 <= 2 * epsilon;
        #}   
        return (math.log(n)/math.log(3) + epsilon) % 1 <= 2*epsilon
    
        #print(log(n, 3), floor(log(n,3)))
        #return log(n, 3) == floor(log(n,3))