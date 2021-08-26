class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        squareSet = set()
        
        for x in range(0, int(math.sqrt(c+1))+ 1):
            #print(x)
            val = x*x
            squareSet.add(val)
            if c - (val) in squareSet:
                return True
            
        return False