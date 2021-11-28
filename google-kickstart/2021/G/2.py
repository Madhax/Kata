import sys
from collections import Counter

sys.setrecursionlimit(10**5)

N = 0
K = 0
bananas = []


@functools.cache
def dp(index, taken):
    
    if index == N:
        return (0,0)

    bestops = math.inf
    bestk = 0

    if taken == 2:
        #we can only skip
        (candops, candk) = dp(index+1, 0)

    else:
        (candops, candk) = dp(index+1, taken+1)
        candops += 1
        candk += bananas[index]

        if candk <= k and candops <= bestops:
            bestops = candops
            bestk = candk

    
    return (bestops, bestk)


def solve():


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        N, K = list(map(int, input().split()))
        bananas = list(map(int, input().split()))

        print(f"Case #{test}: {solve(bananas)}")

"""
1
3
0 0 1 1
2 3 4 6
0 3 5 9
"""