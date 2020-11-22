class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        
        k = len(str(n))
        
       
        res = 0
        
        for i in range(1, k):
            res += len(digits) ** i
            
        largest = list(str(n))
        
        def helper(i):
            
            if i == k:
                return 1
            cnts = 0
            this = largest[i]
            for d in digits:
                if d < this:
                    cnts += len(digits) ** (k-i-1)
            if this in digits:
                cnts += helper(i+1)
            return cnts
        
        res += helper(0)            
            
        return res % (10 ** 9 + 7)