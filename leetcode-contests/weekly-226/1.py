from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = defaultdict(int)
        
        for x in range(lowLimit, highLimit+1):
            num = str(x)
            box = sum(int(c) for c in num)
            d[box] += 1
            
        return max([d[x] for x in d.keys()])