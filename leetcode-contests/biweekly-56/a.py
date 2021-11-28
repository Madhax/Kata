class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        #print(math.ceil(math.sqrt(n))+1)
        def is_square(i: int) -> bool:
            return i == math.isqrt(i) ** 2

        for x in range(1, n+1):
            for y in range(1, n+1):
                if is_square(x**2 + y**2) and 1 <= math.sqrt(x**2+y**2) <= n:
                    cnt += 1
        
        return cnt