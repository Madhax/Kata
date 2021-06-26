from bisect import *
import math
def solve(arr):

    work = [(val, index) for index, val in enumerate(arr)]
    #print(work)
    work.sort()

    ctr = 0
    prevPosn = len(work)
    for x in range(len(work)):
        cand1val, cand1idx = work[x]
        upperLim = int(math.ceil(len(work)/cand1val))*2
        posn = bisect_left(work, (upperLim,0), 0, min(prevPosn+2, len(work)))

        for y in range(min(posn+1, len(work)-1), x, -1):
            cand2val, cand2idx = work[y]

            if cand1val * cand2val == cand1idx+cand2idx+2:
                ctr += 1

        prevPosn = posn

    return ctr


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = int(input())
        arr = map(int, input().split())
        print(f"{solve(arr)}")

"""
3
2
3 1
3
6 1 5
5
3 1 5 9 2


1
2
5 4 3 2 1
"""