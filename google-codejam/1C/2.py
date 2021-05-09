import math
def solve(year):
    year = str(year)
    best = math.inf

    for x in range(1, 100000):
        start = x 
        buildStr = str(start)
        while int(buildStr) <= int(year):
            start += 1
            buildStr += str(start)

        if int(buildStr) < best:
            best = int(buildStr)
    
    return best




if __name__ == "__main__":
    tests = int(input())
    for t in range(1, tests+1):
        val = int(input())
        print(f"Case #{t}: {solve(val)}")

"""
from functools import *
import sys
import math

X, Y, Pattern = 0, 0, []
sys.setrecursionlimit(3000)

@lru_cache(maxsize=20000)
def dp(index, isJ):
    if index == len(Pattern):
        return 0
        
    retVal = math.inf

    if Pattern[index] == "J":
        if isJ:
            return dp(index+1, True)
        else:
            return X + dp(index+1, True)
    elif Pattern[index] == "C":
        if isJ:
            return Y + dp(index+1, False)
        else:
            return dp(index+1, False)
        
    else:
        if isJ:
            #choose J
            retVal = min(retVal, dp(index+1, True))
            #choose C
            retVal = min(retVal, Y + dp(index+1, False))
        else:
            #choose J
            retVal = min(retVal, X + dp(index+1, True))
            #choose C
            retVal = min(retVal, dp(index+1, False))
            
    return retVal
    

if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        dp.cache_clear()
        X, Y, Pattern = input().split()
        X = int(X)
        Y = int(Y)
        Pattern = list(Pattern)
        soln = math.inf
        if Pattern[0] == "J":
            soln = dp(1, True)
        elif Pattern[0] == "C":
            soln = dp(1, False)
        else:
            soln = min(dp(1, False), dp(1, True))

        print(f"Case #{test}: {soln}")
"""