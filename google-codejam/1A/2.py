import math
import sys
from functools import *

sys.setrecursionlimit(3000)


def solve(d, curSum, curProduct):
    remSum = curSum

    @lru_cache(maxsize=None)
    def helper(curProduct):
        nonlocal remSum

        if curProduct > remSum:
            return 0

        if curProduct == remSum:
            return curProduct

        best = 0
        
        for key in sorted(d.keys(), reverse=True):
            if d[key] > 0:
                remSum -= key
                d[key] -= 1
                best = max(best, helper(curProduct*key))

                d[key] += 1
                remSum += key

        return best
        
    helper.cache_clear()
    return helper(1)


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        primes = int(input())
        d = {}
        curSum = 0
        curProduct = 1
        for x in range(primes):
            
            prime, count = list(map(int, input().split()))
            d[prime] = count
            curSum += (prime*count)
            curProduct *= (prime**count)
            #print(curProduct)
        print(f"Case #{test}: {solve(d, curSum, curProduct)}")