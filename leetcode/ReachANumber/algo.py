class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = ceil(sqrt(2*target)-1)
        while True:
            upper = n * (n+1) // 2
            if upper >= target and (upper - target) % 2 == 0:
                break
            n += 1
        return n