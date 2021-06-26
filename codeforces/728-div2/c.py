from bisect import *
import math
def solve(arr):

    arr.sort()
    cost = 0
    for x in range(1, len(arr)):
        cost += (arr[x] - arr[x-1])
        print(arr[x] - arr[x-1])

    cost += (arr[0] - arr[-1])
    return cost


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t + 1):
        _ = int(input())
        arr = list(map(int, input().split()))
        print(f"{solve(arr)}")

"""
3
3
0 2 3
2
0 1000000000
1
0



1
3
0 2 3
"""