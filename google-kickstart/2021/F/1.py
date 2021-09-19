import sys
import math
sys.setrecursionlimit(10**5)

def solve(strVal):
    N = len(strVal)

    l = [math.inf]*N
    #print(N, l)
    prevTrash = math.inf

    for idx, c in enumerate(strVal):
        if c == "1":
            prevTrash = 0
        else:
            prevTrash += 1
        #print(idx, l)
        l[idx] = prevTrash
        

    r = [math.inf]*N

    for idx, c in enumerate(reversed(strVal)):
        if c == "1":
            prevTrash = 0
        else:
            prevTrash += 1

        r[idx] = prevTrash

    r.reverse()

    bests = [math.inf]*N
    for idx, (cand1, cand2) in enumerate(zip(l,r)):
        bests[idx] = min(cand1, cand2)

    return sum(bests)


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        
        _ = int(input())
        strVal = str(input())

        print(f"Case #{test}: {solve(strVal)}")

"""
2
start
jjj
"""