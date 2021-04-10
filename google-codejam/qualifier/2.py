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