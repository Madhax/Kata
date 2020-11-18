class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        x = p // math.gcd(p, q)
        y = q // math.gcd(p, q)
        
        if x % 2 == 1 and y % 2 == 1:
            return 1
        elif x % 2 == 0 and y % 2 == 1:
            return 2
        else:
            return 0