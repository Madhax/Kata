import sys
import math
import bisect

sys.setrecursionlimit(10**5)

def solve(K,attractions):

    attractions.sort()
    best = 0
    eventiter = 0
    curDay = -1

    topk = []
    curTop = 0
    while eventiter < len(attractions):
        curDay = attractions[eventiter][0]

        while eventiter < len(attractions) and attractions[eventiter][0] == curDay:
            _, v = attractions[eventiter]
            #print(topk, curTop)
            if v > 0:
                
                bisect.insort(topk, v)
                if topk[-K:][0] <= v:
                    curTop += v
                    if len(topk) > K:
                        curTop -= topk[-(K+1):][0]
            else:
                didx = bisect.bisect_left(topk, -v)
                if topk[-K:][0] <= -v:
                    #print("here")
                    curTop += v
                    if len(topk) > K:
                        curTop += topk[-(K+1):][0]
                del topk[didx]

            eventiter += 1
            best = max(best, curTop)

    return best
    
if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        
        D,N,K = list(map(int, input().split()))
        attractions = []
        for _ in range(N):
            v,s,e = list(map(int, input().split()))
            attractions.append((s,v))
            attractions.append((e+1,-v))
        
        print(f"Case #{test}: {solve(K,attractions)}")

"""
2
10 4 2
800 2 8
1500 6 9
200 4 7
400 3 5

1
5 3 3
400 1 3
500 5 5
300 2 3
"""